from __future__ import unicode_literals

from commons.models import *
from asset.models import Asset


class Warehouse(Base):
    name = models.CharField(max_length=64)
    curator = models.ForeignKey(User, related_name="%(class)s_curator")
    address = models.ForeignKey(Contact,related_name="%(class)s_address")
    remark = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class WarehouseAssets(Base):
    warehouse = models.ForeignKey(Warehouse,related_name="%(class)s_warehouse")
    asset = models.ForeignKey(Asset,related_name="%(class)s_asset")
    amount = models.PositiveIntegerField()
    remark = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ("warehouse","asset")
        verbose_name_plural = "Warehouse Assets"

    def __unicode__(self):
        return self.asset.name + "(" + self.warehouse.name + ")"






