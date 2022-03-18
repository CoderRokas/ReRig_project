from django import forms
from django.contrib.auth.models import User
import datetime
from rerig.models import Post,Review,Profile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'password',)

class UpdateProfileForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Profile
        fields = ('picture',)

class PostForm(forms.ModelForm):

    categoryChoices = ('PC', 'Laptop',)

    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200, help_text="Please enter a description of your build.")
    averageRating = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    category = forms.MultipleChoiceField(choices=categoryChoices)
    picture = forms.ImageField()

    class Meta:
        model = Post
        fields = ('title', 'averageRating', 'category', 'picture',)

class ReviewForm(forms.ModelForm):
    comment = forms.CharField(max_length=200)
    score = forms.IntegerField(max_value=5)

    class Meta:
        model = Review
        fields = ('comment', 'score',)
