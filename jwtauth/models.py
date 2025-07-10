from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Subject(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='subject_images/' , blank=True , null=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/' , blank=True , null=True)
    owner = models.ForeignKey(User , on_delete=models.CASCADE , related_name='owner')
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE , related_name='subject')

    def __str__(self):
        return self.title


# Create your models here.
