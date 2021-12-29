from django.db import models

# Create your models here.

class App5Notes(models.Model):
    
    body = models.TextField()
    
    def __str__(self):
        return self.body