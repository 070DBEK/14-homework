from django.db import models
from django.urls import reverse


class Subject(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    def get_detail_url(self):
        return reverse('subjects:detail', args=[self.pk])
