from django.db import models

# Create your models here.
class Sample(models>model):

    user = models.CharField()
    password = models.CharField()

    def __unicode__(self):

        return self.user
