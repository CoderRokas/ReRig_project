from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='profile_images/default.png', upload_to='profile_images')
    slug = models.SlugField(default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.user.username)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    averageRating = models.IntegerField(default=0)
    category = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    picture = models.ImageField(default='post_images/default.png', upload_to='post_images')

    def __str__(self):
        return self.title

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.comment