from django.db import models

CATEGORY_CHOICES = (
    (1, 'Facebook'),
    (2, 'Weibo'),
)
# Create your models here.
class AcctModel(models.Model):
    category = models.IntegerField(choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    passwd = models.CharField(max_length=50)

class KeywordModel(models.Model):
    category = models.IntegerField(choices=CATEGORY_CHOICES)
    word = models.CharField(max_length=50)