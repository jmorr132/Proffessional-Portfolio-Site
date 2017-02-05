from django.db import models

# Database for Blog Posts
class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField() 
    date = models.DateTimeField()

    def __str__(self):
        return self.title

