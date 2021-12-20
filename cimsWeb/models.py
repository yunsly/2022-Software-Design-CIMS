from django.db import models


class SocialDistanceLevelOfRegion(models.Model):
    region = models.CharField(max_length=100)
    level = models.IntegerField()
    term = models.CharField(max_length=100)


class MetroCity(SocialDistanceLevelOfRegion):
    pass


class Do(SocialDistanceLevelOfRegion):
    pass


class SelfGoverningDo(SocialDistanceLevelOfRegion):
    pass


class SelfGoverningSi(SocialDistanceLevelOfRegion):
    pass


class Si(SocialDistanceLevelOfRegion):
    pass


class Gun(SocialDistanceLevelOfRegion):
    pass


class SocialDistanceLevel(models.Model):
    level = models.CharField(max_length=1000)
    criterion = models.CharField(max_length=1000)
    privateMeetingRule = models.CharField(max_length=1000)
    festivalRule = models.CharField(max_length=1000)
    rallyRule = models.CharField(max_length=1000)


# Create your models here.
class CoronicStatusOfRegion(models.Model):
    #"""Model representing a Coronic Status of Region."""
    region = models.CharField(max_length=100)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    coronicCount = models.IntegerField()
    coronicGap = models.IntegerField()

    def __str__(self):
        #    """String for representing the Model object."""
        return f'{self.region} : {self.coronicCount}({self.coronicGap})'

class CoronicStatusOfKorea(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    coronicCount = models.IntegerField()
    coronicGap = models.IntegerField()
    
    def __str__(self):
        #    """String for representing the Model object."""
        return f'{self.coronicCount}({self.coronicGap})'
