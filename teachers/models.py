from django.db import models
from django.db.models import CASCADE
from subjects.models import BaseModel, Subject
from django.urls import reverse


class Teacher(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    experience = models.PositiveIntegerField()
    image = models.ImageField(upload_to='teachers_images/')
    subject = models.ForeignKey(Subject, on_delete=CASCADE, related_name='teachers')


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    def get_detail_url(self):
        return reverse('teachers:detail', args=[self.pk])


    def get_update_url(self):
        return reverse('teachers:update', args=[self.pk])


    def get_delete_url(self):
        return reverse('teachers:delete', args=[self.pk])
