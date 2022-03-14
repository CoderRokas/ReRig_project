from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='profile_images/default.png', upload_to='profile_images')
    
    def __str__(self):
        return str(self.user.username)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    averageRating = models.IntegerField(default=0)
    category = models.CharField(max_length=50)
    date = models.DateField()
    picture = models.ImageField(default='post_images/default.png', upload_to='post_images')

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.comment