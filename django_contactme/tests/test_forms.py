import time

from django.test import TestCase

from django_contactme.forms import ContactMsgSecurityForm, ContactMsgForm


class ContactMsgSecurityFormTestCase(TestCase):

    def test_constructor(self):
        # timestamp and security_hash calculated during construction
        form = ContactMsgSecurityForm()
        self.assert_(form.initial.get("timestamp", None) is not None)
        self.assert_(form.initial.get("security_hash", None) is not None)
        self.assert_(form.initial.get("honeypot", None) is None)

        # even though they were provided as initial data
        initial = {'timestamp': '1122334455', 'security_hash': 'blahblahashed'}
        form = ContactMsgSecurityForm(initial=initial.copy())
        self.assert_(form.initial["timestamp"] != initial["timestamp"])
        self.assert_(form.initial["security_hash"] != initial["security_hash"])

    def test_clean_timestamp(self):
        # check that a timestamp more than two hours old is not accepted
        form = ContactMsgSecurityForm()
        timestamp = int(form.initial["timestamp"]) - (2 * 60 * 61)
        security_hash = form.generate_security_hash(timestamp)
        data = {"timestamp": str(timestamp), "security_hash": security_hash}
        form = ContactMsgSecurityForm(data=data)
        self.assert_(form.errors.get("timestamp", None) is not None)

    def test_clean_security_hash(self):
        # check that changing the timestamp invalidates the security_hash
        form = ContactMsgSecurityForm()
        data = {"timestamp": str(time.time()),
                "security_hash": form.initial["security_hash"]}
        form = ContactMsgSecurityForm(data=data)
        self.assert_(form.errors.get("security_hash", None) is not None)

    def test_clean_honeypot(self):
        # check that validation error raises when honeypot is not empty
        form = ContactMsgSecurityForm()
        data = {"honeypot": "Oh! big mistake!"}
        data.update(form.initial)
        form = ContactMsgSecurityForm(data=data)
        self.assert_(form.errors.get("honeypot", None) is not None)


MESSAGE = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean "
           "pulvinar, diam quis iaculis placerat, quam tellus ullamcorper "
           "risus, a accumsan lectus dui id nisi. Nulla nisi nulla, feugiat "
           "at malesuada ut, commodo sollicitudin urna. Sed adipiscing "
           "aliquam metus a scelerisque. Proin in erat ut lectus gravida "
           "rutrum. Sed vel eros id turpis convallis scelerisque ut nec "
           "nisl. Morbi et odio id ante ullamcorper ultrices. Nulla odio "
           "dui, ultricies a egestas nec, aliquet at ligula. Vestibulum "
           "scelerisque turpis mollis arcu suscipit laoreet. Suspendisse "
           "faucibus erat fermentum tortor facilisis aliquam. Donec vitae "
           "arcu elit. In hac habitasse platea dictumst. Morbi congue "
           "scelerisque lobortis.")


class ContactMsgFormTestCase(TestCase):

    def test_get_instance_data(self):
        # check get_contact_msg raises ValueError when form is not valid
        form = ContactMsgForm()
        name = 'Alice Bloggs'
        email = 'alice.bloggs@example.com'
        data = {'name': name, 'email': email, 'message': MESSAGE}
        data.update(form.initial)
        form = ContactMsgForm(data=data)
        form.is_valid()
        data = form.get_instance_data()
        self.assert_(len(data) == 4)
        self.assert_(name == data['name'])
        self.assert_(email == data['email'])
        self.assert_(MESSAGE == data['message'])
