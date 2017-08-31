"""parameters used by PCSE in normalised form"""

from django.db import models
from simulation.models.general_models import ScenarioSpecificBase
from django.forms.models import model_to_dict
from .location_models import PCSESoilParameters, PCSESiteParameters

class PCSECropParameters(ScenarioSpecificBase):
    DVSI = models.FloatField()
    WLVGI = models.FloatField()
    WSTI = models.FloatField()
    WRTLI = models.FloatField()
    WSOI = models.FloatField()

    # initial rooting depth
    ROOTDI = models.FloatField()

    DVSDR = models.FloatField()  # Development stage above which death of leaves and roots start.
    DVSNLT = models.FloatField()  # development stage N-limit
    DVSNT = models.FloatField()  # development stage N-threshold
    FNTRT = models.FloatField()  # Nitrogen translocation from roots as a fraction of the total amount of nitrogen translocated from leaves and stem.
    FRNX = models.FloatField()  # Optimal N concentration as the fraction of maximum N concentration.
    K = models.FloatField()  # light extinction coefficient
    LAICR = models.FloatField()  # (oC d)-1, critical LAI above which mutual shading of leaves occurs,
    LRNR = models.FloatField()
    LSNR = models.FloatField()
    LUE = models.FloatField()  # Light use efficiency.
    NFRLVI = models.FloatField()  # Initial fraction of N (g N g-1 DM) in leaves.
    NFRRTI = models.FloatField()  # Initial fraction of N (g N g-1 DM) in roots.
    NFRSTI = models.FloatField()  # Initial fraction of N (g N g-1 DM) in stem.
    NLAI = models.FloatField()  # Coefficient for the effect of N stress on LAI reduction(during juvenile phase)
    NLUE = models.FloatField()  # Extinction coefficient for  Nitrogen distribution down the canopy
    NMAXSO = models.FloatField()
    NPART = models.FloatField()  # Coefficient for the effect of N stress on leaf biomass reduction
    NSLA = models.FloatField()  # Coefficient for the effect of N stress on SLA reduction
    RDRRT = models.FloatField()  # Relative death rate of roots.
    RDRSHM = models.FloatField()  # and the maximum relative death rate of leaves due to shading.
    RGRL = models.FloatField()  # Relative growth rate of LAI at the exponential growth phase
    RNFLV = models.FloatField()  # Residual N concentration in leaves
    RNFRT = models.FloatField()  # Residual N concentration in roots.
    RNFST = models.FloatField()  # Residual N concentration in stem
    ROOTDM = models.FloatField()  # Maximum root depth
    RRDMAX = models.FloatField()  # Maximum rate of increase in rooting depth (m d-1).
    SLAC = models.FloatField()  # Specific leaf area constant.
    TBASE = models.FloatField()  # Base temperature for spring wheat crop.
    TCNT = models.FloatField()  # Time coefficient(days) for N translocation.
    TRANCO = models.FloatField()  # Transpiration constant (mm/day) indicating the level of drought tolerance of the wheat crop.
    TSUMAG = models.FloatField()  # Temperature sum for ageing of leaves

    #  phenology
    TBASEM = models.FloatField()  # lower threshold temp. for emergence [cel]
    TEFFMX = models.FloatField()  # max. eff. temp. for emergence [cel]
    TSUMEM = models.FloatField()  # temperature sum from sowing to emergence [cel d]
    IDSL = models.IntegerField(choices=((0,"temperature"),(1,"day length"),(2,"both")))  # indicates whether pre-anthesis development depends
    # on temp. (=0), daylength (=1) , or both (=2)
    DLO = models.FloatField()  # optimum daylength for development [hr]
    DLC = models.FloatField()  # critical daylength (lower threshold) [hr]
    TSUM1 = models.FloatField()  # temperature sum from emergence to anthesis [cel d]
    TSUM2 = models.FloatField()  # temperature sum from anthesis to maturity [cel d]
    DVSI = models.IntegerField() # development stage start simulation (after transplanting)
    DVSEND = models.FloatField()  # development stage at harvest or at
    # physiological maturity (= 2.0 at maturity [-])

    #  Relative death rate of leaves due to N stress.
    RDRNS = models.FloatField()

    #  Relative death rate of roots.
    RDRRT = models.FloatField()

    def to_dict(self):
        d = model_to_dict(self)
        d["DTSMTB"]=self.DTSMTB.list()
        d["RDRT"]=self.RDRT.list()
        d["SLACF"]=self.SLACF.list()
        d["NMXLV"]=self.NMXLV.list()
        d["FRTTB"]=self.FRTTB.list()
        d["FLVTB"]=self.FLVTB.list()
        d["FSTTB"]=self.FSTTB.list()
        d["FSOTB"]=self.FSOTB.list()
        return d

    class Meta:
        verbose_name_plural = "crop parameter sets"


class ParametersSetBase(models.Model):
    def list(self):
        d =model_to_dict(self)
        return [v for v in d.values()]

    class Meta:
        abstract=True


class CropParametersDTSMTB(ParametersSetBase):
    """daily increase in temp. sum as function of av. temp. [cel; cel d]"""
    crop = models.OneToOneField(PCSECropParameters, on_delete=models.CASCADE, primary_key=True, related_name="DTSMTB")
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    d = models.FloatField()


class CropParametersRDRT(ParametersSetBase):
    """Interpolation functions"""
    crop = models.OneToOneField(PCSECropParameters, on_delete=models.CASCADE, primary_key=True, related_name="RDRT")
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    d = models.FloatField()
    e = models.FloatField()
    f = models.FloatField()
    g = models.FloatField()
    h = models.FloatField()
    i = models.FloatField()
    j = models.FloatField()

class CropParametersSLACF(ParametersSetBase):
    """Leaf area correction function as a function of development stage, DVS"""
    crop = models.OneToOneField(PCSECropParameters, on_delete=models.CASCADE, primary_key=True, related_name="SLACF")
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    d = models.FloatField()
    e = models.FloatField()
    f = models.FloatField()


class CropParametersNMXLV(ParametersSetBase):
    """Maximum N concentration in the leaves, from which the N-conc.values of the stem and roots are derived, as a function of development stage."""
    crop = models.OneToOneField(PCSECropParameters, on_delete=models.CASCADE, primary_key=True, related_name="NMXLV")
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    d = models.FloatField()
    e = models.FloatField()
    f = models.FloatField()
    g = models.FloatField()
    h = models.FloatField()
    i = models.FloatField()
    j = models.FloatField()
    k = models.FloatField()
    l = models.FloatField()


# ********** Partitioning coefficients ***********************************
class CropParametersFRTTB(ParametersSetBase):
    crop = models.OneToOneField(PCSECropParameters, on_delete=models.CASCADE, primary_key=True, related_name="FRTTB")
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    d = models.FloatField()
    e = models.FloatField()
    f = models.FloatField()
    g = models.FloatField()
    h = models.FloatField()
    i = models.FloatField()
    j = models.FloatField()
    k = models.FloatField()
    l = models.FloatField()


class CropParametersFLVTB(ParametersSetBase):
    crop = models.OneToOneField(PCSECropParameters, on_delete=models.CASCADE, primary_key=True, related_name="FLVTB")
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    d = models.FloatField()
    e = models.FloatField()
    f = models.FloatField()
    g = models.FloatField()
    h = models.FloatField()
    i = models.FloatField()
    j = models.FloatField()
    k = models.FloatField()
    l = models.FloatField()
    m = models.FloatField()
    n = models.FloatField()


class CropParametersFSTTB(ParametersSetBase):
    crop = models.OneToOneField(PCSECropParameters, on_delete=models.CASCADE, primary_key=True, related_name="FSTTB")
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    d = models.FloatField()
    e = models.FloatField()
    f = models.FloatField()
    g = models.FloatField()
    h = models.FloatField()
    i = models.FloatField()
    j = models.FloatField()
    k = models.FloatField()
    l = models.FloatField()
    m = models.FloatField()
    n = models.FloatField()


class CropParametersFSOTB(models.Model):
    crop = models.OneToOneField(PCSECropParameters, on_delete=models.CASCADE, primary_key=True, related_name="FSOTB")
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    d = models.FloatField()
    e = models.FloatField()
    f = models.FloatField()
    g = models.FloatField()
    h = models.FloatField()
    i = models.FloatField()
    j = models.FloatField()
    k = models.FloatField()
    l = models.FloatField()
    m = models.FloatField()
    n = models.FloatField()

class CropInstance(ScenarioSpecificBase):
    crop = models.OneToOneField(PCSECropParameters)
    soil = models.OneToOneField(PCSESoilParameters)
    site = models.OneToOneField(PCSESiteParameters)
