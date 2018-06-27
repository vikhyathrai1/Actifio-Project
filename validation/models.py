from django.db import models

# Create your models here.

# class Inventory(models.Model):
#     data=models.Field(max_length=255,blank=False)
#
#     def __str__(self):
#         return '{}'.format(self.data)

class SimpleData(object):
    data = []

    def __init__(self):
        self.data = []

    def add(self, data):
        self.data.append(data)

