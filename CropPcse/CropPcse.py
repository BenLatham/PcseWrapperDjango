from pcse.db import NASAPowerWeatherDataProvider
from CropPcse import models


class CropPcse:
    def __init__(self, scenario):
        cropdata = models.PCSECropParameters.objects.get(scenario=scenario).to_dict()
        soildata = models.PCSESoilParameters.objects.get(scenario=scenario).to_dict()
        sitedata = models.PCSESiteParameters.objects.get(scenario=scenario).to_dict()
        agromanagement =
        wdp = NASAPowerWeatherDataProvider(latitude=52, longitude=5)

