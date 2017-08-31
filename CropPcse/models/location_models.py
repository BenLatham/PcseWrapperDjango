from django.db import models
from simulation.models.general_models import ScenarioSpecificBase
from django.forms.models import model_to_dict

class PCSESoilParameters(ScenarioSpecificBase):
    # Soil hydraulic properties
    WCAD   = models.FloatField(help_text = "Water content at air dry")
    WCWP   = models.FloatField(help_text ="Water content at wilting point")
    WCFC   = models.FloatField(help_text = "Water content at field capacity")
    WCWET  = models.FloatField(help_text = "Water content at above which oxygen stress occurs")
    WCST   = models.FloatField(help_text = "Water content at saturation")
    DRATE  = models.FloatField(help_text = "Maximum drainage rate of the soil (mm/day)")

    def to_dict(self):
        return model_to_dict(self)

    class Meta:
        verbose_name_plural = "soil parameter sets"


class PCSESiteParameters(ScenarioSpecificBase):
    # initial soil conditions
    WCI = models.FloatField(help_text="Initial water content in cm3 of water/(cm3 of soil).")
    WCSUBS = models.FloatField(help_text="water content subsoil")

    # Water management
    # We will represent two water management situations in the model
    # as irrigated up to the field capacity:  WMFAC
    # as irrigated up to saturation, thus mimicking flooding; WMFAC
    # In both cases parameter IRRIGF must be taken 1.0. "Irrigation"
    WMFAC  = models.BooleanField(help_text="irrigated to field capacity")
    IRRIGF = models.BooleanField(help_text="irrigated up to saturation(mimicing flooding)")

    def to_dict(self):
        return model_to_dict(self)

    class Meta:
        verbose_name_plural = "site parameter sets"
