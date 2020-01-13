from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
            return self.first_name

    def save_author(self):
            self.save()
    class Meta:
        ordering = ['first_name']


class Project(models.Model):
    title = models.CharField(max_length=60)
    post = HTMLField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    caption = models.CharField(max_length=150)
    pub_date = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(upload_to='projects/',blank=True)

    @classmethod
    def search_by_title(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects
    
    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects


class ProjectsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

    @classmethod
    def todays_projects(cls):
        today = dt.date.today()
        projects = cls.objects.filter(pub_date__date = today)
        return projects
    @classmethod
    def days_projects(cls,date):
        projects = cls.objects.filter(pub_date__date = date)
        return projects

class MoringaMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()