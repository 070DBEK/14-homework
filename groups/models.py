from django.db import models
from subjects.models import BaseModel
from teachers.models import Teacher
from django.urls import reverse


class Group(BaseModel):
    name = models.CharField(max_length=100)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    students = models.TextField()

    def __str__(self):
        return self.name

    def get_detail_url(self):
        return reverse('groups:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('groups:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('groups:delete', args=[self.pk])