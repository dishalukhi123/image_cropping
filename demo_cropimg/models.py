from django.db import models

class Images(models.Model):
    image = models.ImageField()
    square = models.ImageField()
    rectangle = models.ImageField()


    def __str__(self):
        return str(self.pk)
    
    class Meta:
        db_table = 'images'

