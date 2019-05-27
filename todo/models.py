from django.db import models

# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length=40)

    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural='todo\'s'

class Programmers(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 
    class Meta:
        verbose_name_plural = "Programers"
