from __future__ import unicode_literals
# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Base(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    createdby=models.ForeignKey(User,related_name="%(app_label)s_%(class)s_creator")
    modifiedby=models.ForeignKey(User,related_name="%(app_label)s_%(class)s_editor")
    deleted=models.BooleanField(default=False)

    class Meta:
        abstract=True


class Contact(Base):
    care_of_person = models.CharField(null=True,blank=True,max_length=64,verbose_name="C/O")
    street = models.CharField(max_length=64)
    house_no = models.IntegerField()
    post_code = models.IntegerField()
    city = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    phone = models.CharField(null=True,blank=True,max_length=64,verbose_name="Telephone")
    mobile = models.CharField(null=True,blank=True,max_length=128)
    one_liner_address = models.TextField(null=True,blank=True)
    remark = models.TextField(null=True,blank=True)

    def __unicode__(self):
        return "%s, %s %s, %s %s" % (self.care_of_person, self.street, self.house_no, self.post_code,
                                     self.city) if self.care_of_person != "" else "%s %s, %s %s" % (
        self.street, self.house_no, self.post_code, self.city)

    def address(self):
        return "%s, %s %s, %s %s" % (self.care_of_person, self.street, self.house_no, self.post_code,
                                     self.city) if self.care_of_person != "" else "%s %s, %s %s" % (
        self.street, self.house_no, self.post_code, self.city)
    address.short_description = 'Address'
