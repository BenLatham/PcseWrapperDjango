from django.contrib import admin
from . import models

class DTSMTBInline(admin.TabularInline):
    model = models.CropParametersDTSMTB


class RDRTInline(admin.TabularInline):
    model = models.CropParametersRDRT


class SLACFInline(admin.TabularInline):
    model = models.CropParametersSLACF


class NMXLVInline(admin.TabularInline):
    model = models.CropParametersNMXLV


class FRTTBInline(admin.TabularInline):
    model = models.CropParametersFRTTB


class FLVTBInline(admin.TabularInline):
    model = models.CropParametersFLVTB


class FSTTBInline(admin.TabularInline):
    model = models.CropParametersFSTTB


class FSOTBInline(admin.TabularInline):
    model = models.CropParametersFSOTB


class CropParamsAdmin(admin.ModelAdmin):
    inlines = [
        DTSMTBInline, RDRTInline, SLACFInline, NMXLVInline, FRTTBInline, FLVTBInline, FSTTBInline, FSOTBInline
    ]

admin.site.register(models.PCSECropParameters, CropParamsAdmin)
admin.site.register(models.PCSESiteParameters)
admin.site.register(models.PCSESoilParameters)
admin.site.register(models.CropInstance)
admin.site.register(models.Campaign)
admin.site.register(models.CropCalender)
admin.site.register(models.Irrigation)
admin.site.register(models.Fertilization)