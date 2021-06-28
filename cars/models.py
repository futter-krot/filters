from django.db import models

# Create your models here.


class Car(models.Model):
    producer = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    series_date = models.IntegerField()
    transmission = models.SmallIntegerField(choices=[(1, 'Manual'), (2, 'Automatic'), (3, 'Robotic')])
    color = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.model} {self.producer}'

