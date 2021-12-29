from django.db import models

# Create your models here.
class App2(models.Model):
    body = models.TextField(null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body