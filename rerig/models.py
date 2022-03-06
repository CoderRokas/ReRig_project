from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    NAME_MAX_LENGTH = 30
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    username = models.CharField(max_length=NAME_MAX_LENGTH)
    password = models.CharField(max_length=NAME_MAX_LENGTH)
    # picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    averageRating = models.IntegerField(default=0)
    category = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.CharField(max_length=200)
    date = models.DateField()