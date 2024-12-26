from django.db import models
from django.shortcuts import reverse



class Track(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    data = models.DateField()
    image = models.ImageField(upload_to='music_image/')
    file = models.FileField(upload_to='music_file/')

    def get_detail_url(self):
        return reverse('tracks:detail', args=[self.pk])