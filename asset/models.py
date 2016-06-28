from __future__ import unicode_literals
from commons.models import *


class AssetGroup(Base):
    name = models.CharField(max_length=64)
    remark = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class AssetBrand(Base):
    name = models.CharField(max_length=64)
    remark = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class Asset(Base):
    name = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    serial = models.CharField(max_length=64)
    size = models.CharField(max_length=32, null=True,blank=True)
    color = models.CharField(max_length=32,null=True,blank=True)
    image = models.ImageField(upload_to="asset", null=True,blank=True)
    asset_group = models.ForeignKey(AssetGroup,related_name="%(class)s_group")
    asset_brand = models.ForeignKey(AssetBrand, related_name="%(class)s_brand")
    remark = models.TextField(null=True, blank=True)


    def __unicode__(self):
        return self.asset_brand.name+" "+self.name

    def show_spec(self):
        return "Size: %s & Color: %s" % (self.size,self.color)
    show_spec.short_description = "Specs"


