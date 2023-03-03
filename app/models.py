from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Representative(models.Model):
    
    document = models.CharField(max_length=10, null=True, blank=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(max_length=12, null=True)
    # address = models.TextField()
    
    def __str__(self):
        return f'{self.user_id.first_name} {self.user_id.last_name}'


class Professor(models.Model):
    
    document = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=12, null=True)
    address = models.TextField()
    
    def __str__(self):
        return self.name


class Subject(models.Model):
    
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    professor_ids = models.ManyToManyField(Professor, through='Section')
    
    def __str__(self):
        return self.name


class Section(models.Model):
    
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f'{self.subject_id}, {self.year} year'

    
class Student(models.Model):
    
    representative_ids = models.ManyToManyField(Representative)
    section_ids = models.ManyToManyField(Section, through='Inscription')
    document = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=25)
    address = models.TextField()
    age = models.PositiveSmallIntegerField()
    birth = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name 
    
    
class Qualification(models.Model):
    
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.FloatField()
    
    # def __str__(self):
    #     return f'{self.student_id} - {self.subject_id} - {self.score}'


class Inscription(models.Model):
    
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)