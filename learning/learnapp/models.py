from django.db import models

# Create your models here.
class Student(models.Model):

    GRADES = (
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12')
    )

    first_name = models.CharField(max_length=200, null=True, verbose_name='First Name')
    last_name = models.CharField(max_length=200, null=True, verbose_name='Last Name')
    middle_name = models.CharField(max_length=200, null=True, verbose_name='Middle Name')
    grade = models.CharField(max_length=200, null=True, choices=GRADES, verbose_name='Grade')

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

    first_name = models.CharField(max_length=200, null=True, verbose_name='First Name')
    last_name = models.CharField(max_length=200, null=True, verbose_name='Last Name')
    title = models.CharField(max_length=10, null=True, choices=TITLES, verbose_name='Title')
    department = models.CharField(max_length=30, null=True, choices=DEPARTMENTS, verbose_name='Department')

    def __str__(self):
        return f'{self.title}. {self.last_name}, {self.first_name}'