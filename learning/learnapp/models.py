from django.db import models

# Create your models here.
class Student(models.Model):

    GRADES = (
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12')
    )

    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    middle_name = models.CharField(max_length=200, null=True)
    grade = models.CharField(max_length=200, null=True, choices=GRADES)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'