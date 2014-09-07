from django.db import models
from time import time

def get_upload(instance, filename):
    return "upload_files/%s_%s" % (str(time()).replace('.','_'), filename)

class Video(models.Model):
    judul = models.CharField(max_length=100)
    film = models.FileField(upload_to=get_upload)
    pengarang = models.CharField(max_length=100)

    def __unicode__(self):
        return self.judul
