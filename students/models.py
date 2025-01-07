from django.db import models
from groups.models import Group


class Student(models.Model):
    full_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    photo = models.ImageField(upload_to='students-images/', blank=True, null=True)
    group = models.ManyToManyField(Group, blank=True, related_name='student_groups')

    def __str__(self):
        return self.full_name
