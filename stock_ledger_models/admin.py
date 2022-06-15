from django.contrib import admin

from . import models

admin.site.register(models.stg_trn_data)
admin.site.register(models.Location)
admin.site.register(models.Currency)
admin.site.register(models.stg_trn_data_del_records)
admin.site.register(models.Dept)
admin.site.register(models.Class)
admin.site.register(models.SubClass)
admin.site.register(models.ITEM_DTL)
