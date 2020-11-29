from django.db import models


class Student(models.Model):
    name = models.CharField('Name', max_length=50)
    document = models.CharField('Document', max_length=9)

    def __str__(self):
        return self.name
