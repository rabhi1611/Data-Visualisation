from django.db import models
from sklearn import model_selection

# Create your models here.
class data(models.Model):
    end_year = models.IntegerField(blank=True, null=True)
    intensity = models.IntegerField( blank=True, null=True)
    sector = models.CharField(max_length=100000000, blank=True, null=True)
    topic = models.CharField(max_length=100000000, blank=True, null=True)
    insight = models.CharField(max_length=100000000, blank=True, null=True)
    url = models.URLField( blank=True, null=True)
    region = models.CharField(max_length=100000000, blank=True, null=True)
    start_year = models.IntegerField(blank=True, null=True)
    impact = models.CharField(max_length=100000000, blank=True, null=True)
    added = models.CharField(max_length=100000000, blank=True, null=True)
    published = models.CharField(max_length=100000000, blank=True, null=True)
    country = models.CharField(max_length=100000000, blank=True, null=True)
    relevance = models.IntegerField( blank=True, null=True)
    pestle = models.CharField(max_length=100000000, blank=True, null=True)
    source = models.CharField(max_length=100000000, blank=True, null=True)
    title = models.CharField(max_length=100000000, blank=True, null=True)
    likelihood = models.IntegerField( blank=True, null=True)

    def __str__(self):
        return self.title