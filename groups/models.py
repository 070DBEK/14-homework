from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.OneToOneField('teachers.Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    students = models.ManyToManyField('students.Student', blank=True, related_name='group_students')


    def __str__(self):
        return self.name
