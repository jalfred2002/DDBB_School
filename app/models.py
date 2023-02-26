from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

class Representative(models.Model):
    
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f'{self.user_id.first_name} {self.user_id.last_name}'


class Subject(models.Model):
    
    name = models.CharField(max_length=30)
    

class Student(models.Model):
    
    name = models.CharField(max_length=25)
    age = models.PositiveSmallIntegerField()
    birth = models.DateField(null=True, blank=True)
    sections = models.ManyToManyField(Subject, through='Section')
    representatives = models.ManyToManyField(Representative)
    
    def __str__(self):
        return self.name 


class Section(models.Model):
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    period = models.PositiveIntegerField()
    
    

class Rating(models.Model):
    
    date = models.DateField(null=True, blank=True)
    score = models.FloatField()
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    