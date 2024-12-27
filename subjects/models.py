from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # Obyekt yaratilgan vaqt
    updated_at = models.DateTimeField(auto_now=True)      # Obyekt o'zgartirilgan vaqt

    class Meta:
        abstract = True  # Bu model ma'lumotlar bazasida jadval yaratmaydi


class Subject(BaseModel):
    name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.name


    def get_detail_url(self):
        return reverse('subjects:detail', args=[self.pk])


    def get_update_url(self):
        return reverse('subjects:update', args=[self.pk])


    def get_delete_url(self):
        return reverse('subjects:delete', args=[self.pk])
