from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    document = models.CharField(max_length=9)

    def __str__(self):
        return self.name
