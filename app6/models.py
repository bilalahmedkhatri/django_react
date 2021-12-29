from django.db import models

# Create your models here.

class App6Model(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name