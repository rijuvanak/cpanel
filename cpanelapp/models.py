from django.db import models

# Create your models here.

class cdb(models.Model):
    cname=models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=50)


class UploadImage(models.Model):
   caption = models.CharField(max_length=200)
   image = models.ImageField(upload_to='images/')


class File(models.Model):
    name = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    varname = models.CharField(max_length=100)
    
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    major = models.CharField(max_length=500)

class Category(models.Model):
    name = models.CharField(max_length=100)
   
class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bname = models.CharField(max_length=100)
