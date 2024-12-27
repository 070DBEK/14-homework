from django.db import models
from groups.models import Group
from subjects.models import BaseModel
from django.urls import reverse


class Student(BaseModel):
    full_name = models.CharField(max_length=150)
    group = models.ManyToManyField(Group, related_name = 'groups')
    date_of_birth = models.DateTimeField()
    phone_number = models.CharField(max_length=25)
    location = models.CharField(max_length=250)
    image = models.FileField()


    def __str__(self):
        return self.full_name


    def get_detail_url(self):
        return reverse('students:detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('students:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('students:update', args=[self.pk])