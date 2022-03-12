from django.db import models
from django.template.defaultfilters import slugify
# from django.contrib.auth.models import User

class User(models.Model):
    NAME_MAX_LENGTH = 30
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    username = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    password = models.CharField(max_length=NAME_MAX_LENGTH)
    # picture = models.ImageField(upload_to='profile_images', blank=True)
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)


    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    averageRating = models.IntegerField(default=0)
    category = models.CharField(max_length=50)
    date = models.DateField()
    # post will need an image field, right now index just shows the title as
    # a proof of concept

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