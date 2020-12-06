from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=100)
    offset = models.DateTimeField(verbose_name='기준일')
    pub_date = models.DateTimeField(default='')

    def __str__(self):
        return self.title


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default='')

    def __str__(self):
        return self.text
