from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'userprofile'