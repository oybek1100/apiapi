from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/' , blank=True , null=True)
    owner = models.ForeignKey(User , on_delete=models.CASCADE , related_name='owner')
    def __str__(self):
        return self.title



class Module(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course , on_delete=models.CASCADE , related_name='modules')
    def __str__(self):
        return self.title
