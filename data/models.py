from django.db import models

# Create your models here.
    
class Entry(models.Model):
    pname = models.CharField(max_length=255)
    pqty = models.PositiveIntegerField()
    pprice = models.PositiveIntegerField()
    def __str__(self):
        return self.pname
