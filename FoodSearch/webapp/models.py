from django.db import models

# Create your models here.
class dataset(models.Model):
    name=models.CharField(max_length=100);
    url=models.CharField(max_length=100);
    description=models.CharField(max_length=1000);
    author=models.CharField(max_length=100);
    ingredients=models.CharField(max_length=1000);
class user(models.Model):
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	pwd=models.CharField(max_length=100);
	zip=models.CharField(max_length=100);
	gender=models.CharField(max_length=100);
	age=models.CharField(max_length=100);

