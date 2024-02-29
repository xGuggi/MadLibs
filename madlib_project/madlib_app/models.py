from django.db import models


# Create your models here.

class Madlib(models.Model):
    name = models.CharField(max_length=50)
    verb = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    noun = models.CharField(max_length=50)
    pronoun = models.CharField(max_length=50)
    adjective = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    template_name = models.CharField(max_length=50, default='default_template.html')

    class Meta:
        app_label = 'madlib_app'
