from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    email = models.EmailField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
