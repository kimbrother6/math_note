from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Sentence(models.Model):
    english_sentence = models.CharField(max_length=200, null=True, blank=True)
    korean_sentence = models.CharField(max_length=200, null=True, blank=True)
    Memorization = models.CharField(max_length=50, null=True, blank=True)
    Classification = models.CharField(max_length=30, null=True, blank=True)