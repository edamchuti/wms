from __future__ import unicode_literals

from commons.models import *
from people.models import Person
from asset.models import Asset


class Incoming(Base):
    returned_by = models.ForeignKey(Person,related_name="%(class)s_returned_by")
    received_by = models.ForeignKey(User, related_name="%(class)s_receiver")
    asset = models.ForeignKey(Asset,related_name="%(class)s_asset")
    amount = models.PositiveIntegerField(help_text="Let's just use 1 as a value to log better!",default=1)
    remark = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Return"
        verbose_name_plural = "Returns"

    def __unicode__(self):
        return self.returned_by.first_name + self.returned_by.last_name

    def return_date(self):
        return self.modified
    return_date.short_description = "Return date"

class Outgoing(Base):
    assigned_to = models.ForeignKey(Person, related_name="%(class)s_assigned_to")
    assigned_by = models.ForeignKey(User, related_name="%(class)s_assigner")
    asset = models.ForeignKey(Asset, related_name="%(class)s_asset")
    amount = models.PositiveIntegerField(help_text="Let's just use 1 as a value to log better!" ,default=1)
    remark = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Borrow"
        verbose_name_plural = "Borrows"

    def __unicode__(self):
        return self.assigned_by.first_name + self.assigned_by.last_name

    def assigned_date(self):
        return self.modified
    assigned_date.short_description = "Assigned date"

