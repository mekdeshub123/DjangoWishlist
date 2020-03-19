#This file provide a simple mapping to the database structure. 
# It contains the essential fields and behaviors of the data that storing.
from django.db import models

# Create your models here.
#place model created with two fields, name and visited
class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name},visited? {self.visited}'
