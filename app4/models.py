from django.db import models

# Create your models here.
class App4Notes(models.Model):
    text_body = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.text_body