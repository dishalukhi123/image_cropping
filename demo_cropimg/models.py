from django.db import models

class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    square = models.ImageField(upload_to='square_images/')
    rectangle = models.ImageField(upload_to='rectangle_images/')


    def __str__(self):
        return str(self.pk)
    
    class Meta:
        db_table = 'images'