from django.db import models

# Create your models here.
class Todo(models.Model):
    fecha = models.DateTimeField()
    texto = models.CharField(max_length=200)
