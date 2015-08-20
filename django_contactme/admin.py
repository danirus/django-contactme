from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from django_contactme.models import ContactMsg


class ContactMsgAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'submit_date')
    fieldsets = (
        (None,          {'fields': ('site',)}),
        (_('Content'),  {'fields': ('name', 'email', 'message',)}),
        (_('Metadata'), {'fields': ('submit_date', 'ip_address')}),
    )
    date_hierarchy = 'submit_date'
    ordering = ('-submit_date',)

admin.site.register(ContactMsg, ContactMsgAdmin)
