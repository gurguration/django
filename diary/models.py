from django.db import models
# Create your models here.

class Entry(models.Model):
    text = models.TextField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Entry: #{}'.format(self.id)
    class Meta:
        verbose_name_plural = 'Entries'