from django.db import models

# Create your models here.
class Builder(models.Model):
    name = models.CharField(max_lenght=100)
    
    