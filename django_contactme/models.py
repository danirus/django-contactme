import datetime

from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


CONTACTME_MSG_MAX_LEN = getattr(settings,'CONTACTME_MSG_MAX_LEN',3000)


class ContactMsg(models.Model):
    """
    An incoming message from a site visitor.
    """
    site = models.ForeignKey(Site)
    name = models.CharField(_("Contact's name"), max_length=100)
    email = models.EmailField(_("Contact's email address"))
    message = models.TextField(_("Message"), max_length=CONTACTME_MSG_MAX_LEN)
    submit_date = models.DateTimeField(_("Date/Time submitted"), default=None)
    ip_address  = models.IPAddressField(_('IP address'), blank=True, null=True)
    
    class Meta:
        db_table = "contactme_contact_msg"
        ordering = ('submit_date',)
        verbose_name = _('contact message')
        verbose_name_plural = _('contact messages')

    def __unicode__(self):
        return "%s: %s..." % (self.name, self.message[:50])

    def save(self, *args, **kwargs):
        if self.submit_date is None:
            self.submit_date = datetime.datetime.now()
        super(ContactMsg, self).save(*args, **kwargs)

    def get_as_text(self):
        """
        Return this comment as plain text. Useful for emails.
        """
        d = {
            'user': self.name,
            'date': self.submit_date,
            'message': self.message,
            'domain': self.site.domain,
        }
        return _('Sent by %(user)s at %(date)s\n\n%(message)s\n\nhttp://%(domain)s') % d

