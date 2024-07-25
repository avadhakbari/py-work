# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)

    def __str__(self):
        return self.username

# class SocietyMember(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     society = models.ForeignKey("Society", on_delete=models.CASCADE)

# class SocietyWatchman(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     society = models.ForeignKey("Society", on_delete=models.CASCADE)

# class Notice(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     society = models.ForeignKey("Society", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

# class Event(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     date = models.DateField()
#     time = models.TimeField()
#     society = models.ForeignKey("Society", on_delete=models.CASCADE)

# class Society(models.Model):
#     name = models.CharField(max_length=255)
#     # Add any other relevant fields for a society