from django.db import models
from django.contrib.auth.models import AbstractUser

class Subject(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)   

    def __str__(self):
        return self.question_text

class Option(models.Model):
    text = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class User(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    
