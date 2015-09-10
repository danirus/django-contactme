from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Field, Fieldset, Layout, Submit

from django_contactme.forms import ContactMsgForm


class CrispyContactMsgForm(ContactMsgForm):
    def __init__(self, *args, **kwargs):
        super(CrispyContactMsgForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'CF'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'contactme-post-contact-form'
        self.helper.label_class = 'col-lg-3 col-md-3'
        self.helper.field_class = 'col-lg-8 col-md-8'
        self.helper.layout = Fieldset(
            "Your contact details",
            'timestamp', 'security_hash', Field('honeypot', wrapper_class="hide"),
            'name', 'email', 'message'
        )
        send = Submit('submit', 'send', data_name="post")
        preview = Submit('preview', 'preview', css_class="btn btn-default")
        preview.field_classes = 'btn btn-default'
        self.helper.add_input(send)
        self.helper.add_input(preview)
