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

class Teacher(models.Model):

    TITLES = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
        ('Miss', 'Miss'),
        ('Mx', 'Mx'),
    )

    DEPARTMENTS = (
        ('English', 'English'),
        ('Math', 'Math'),
        ('Business', 'Business'),
        ('Family and Consumer Sciences', 'Family and Consumer Sciences'),
        ('Social Studies', 'Social Studies'),
        ('Science', 'Science'),
        ('Foreign Language', 'Foreign Language'),
        ('Physical Education', 'Physical Education')
    )

    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=10, null=True, choices=TITLES)
    department = models.CharField(max_length=30, null=True, choices=DEPARTMENTS)

    def __str__(self):
        return f'{self.title}. {self.last_name}, {self.first_name}'