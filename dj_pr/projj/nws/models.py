from django.db import models

# Create your models here.

class Em(models.Model):
    Em_name = models.CharField(max_length=100)
    Em_id = models.CharField(max_length=100)
    Em_salary = models.CharField(max_length=100)
class User(models.Model):
    u_name = models.CharField(max_length=50)
    u_email = models.EmailField(max_length=50)
    u_pass1 = models.CharField(max_length=50)
    u_pass2 = models.CharField(max_length=50)

class Todo(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    completed = models.BooleanField(default=False)    