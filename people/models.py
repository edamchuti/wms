from __future__ import unicode_literals

from commons.models import *


class PersonType(Base):
    name = models.CharField(max_length=64)
    remark = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Assignee Type'
        verbose_name_plural = 'Assignee Types'

    def __unicode__(self):
        return self.name




class Person(Base):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    contact = models.ForeignKey(Contact,related_name="%(class)s_contact")
    person_type = models.ForeignKey(PersonType, related_name="%(class)s_type",verbose_name="Assignee Type")

    class Meta:
        verbose_name = 'Assignee'
        verbose_name_plural = 'Assignees'

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def name(self):
        return self.first_name + " " + self.last_name
    name.short_description = "Name"