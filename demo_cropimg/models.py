from django.db import models

class CroppedImage(models.Model):
    file = models.ImageField(upload_to='images/')
    uploaded = models.DateTimeField(auto_now_add=True)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)


    def __str__(self):
        return str(self.pk)