from simulation.models.general_models import ScenarioSpecificBase
from django.db import models

class Campaign(ScenarioSpecificBase):
    date = models.DateField()

class CropCalender(models.Model):
    campaign = models.OneToOneField(Campaign)
    crop_name =  models.CharField(max_length=20)
    variety_name=  models.CharField(max_length=20)
    crop_start_date = models.DateField()
    crop_start_type=  models.CharField(max_length=20)
    crop_end_date = models.DateField(null=True)
    crop_end_type=  models.CharField(max_length=20)
    max_duration = models.IntegerField(null=True)

class Irrigation(models.Model):
    event_signal = "irrigate"
    name = "Timed irrigation events"
    comment = "All irrigation amounts in cm"
    campaign = models.ForeignKey(Campaign)
    date = models.DateField()
    ammount = models.FloatField()
    efficiency = models.FloatField()

class Fertilization(models.Model):
    event_signal = "apply_npk"
    name ="Timed N / P / K application table"
    comment = "All fertilizer amounts in kg / ha"
    campaign = models.ForeignKey(Campaign)
    date = models.DateField()
    N_amount = models.FloatField()
    N_recovery = models.FloatField()
    P_amount = models.FloatField()
    P_recovery = models.FloatField()
    K_amount = models.FloatField()
    K_recovery = models.FloatField()
