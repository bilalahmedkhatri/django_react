from django.db import models

# Create your models here.
class App3Model(models.Model):
    body_field = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.body_field