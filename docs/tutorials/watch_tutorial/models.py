## This file is part of the Lino project.

from django.db import models
from lino.api import dd
from lino import mixins
from django.utils.translation import ugettext_lazy as _

from lino.modlib.users.mixins import My, UserAuthored


# class Entry(mixins.CreatedModified, UserAuthored):
class Entry(UserAuthored):

    class Meta:
        verbose_name = _("Entry")
        verbose_name_plural = _("Entries")

    subject = models.CharField(_("Subject"), blank=True, max_length=200)
    body = dd.RichTextField(_("Body"), blank=True)
    company = models.ForeignKey('contacts.Company')


class Entries(dd.Table):
    model = Entry

    detail_layout = """
    id user
    company
    subject
    body
    """

    insert_layout = """
    company
    subject
    """


class EntriesByCompany(Entries):
    master_key = 'company'


class MyEntries(My, Entries):
    pass


@dd.receiver(dd.post_startup)
def my_change_watchers(sender, **kw):
    """
    This site watches the changes to Partner, Company and Entry
    """
    self = sender
    
    from lino.modlib.changes.models import watch_changes as wc
    
    # In our example we want to collect changes to Company and Entry
    # objects to their respective Partner.

    wc(self.modules.contacts.Partner)
    wc(self.modules.contacts.Company, master_key='partner_ptr')
    wc(self.modules.watch_tutorial.Entry, master_key='company__partner_ptr')

    # add two application-specific panels, one to Partners, one to
    # Companies:
    self.modules.contacts.Partners.add_detail_tab(
        'changes', 'changes.ChangesByMaster')
    self.modules.contacts.Companies.add_detail_tab(
        'entries', 'watch_tutorial.EntriesByCompany')

