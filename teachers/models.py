from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE, related_name='teachers')
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    experience = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='teachers-images/')


    def __str__(self):
        return f"{self.first_name} {self.last_name}"