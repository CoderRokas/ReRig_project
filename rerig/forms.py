from django import forms
from django.contrib.auth.models import User
import datetime
from rerig.models import Post,Review

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)

class PostForm(forms.ModelForm):

    categoryChoices = ('PC', 'Laptop')

    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200, help_text="Please enter a description of your build.")
    averageRating = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    category = forms.MultipleChoiceField(choices=categoryChoices)
    date = forms.DateField(widget=forms.HiddenInput(), initial=datetime)

    class Meta:
        model = Post
        fields = ('title', 'averageRating', 'category',)

class ReviewForm(forms.ModelForm):
    comment = forms.CharField(max_length=200)
    score = forms.IntegerField(max_value=5)
    date = forms.DateField(widget=forms.HiddenInput(), initial=datetime)

    class Meta:
        model = Review
        fields = ('comment', 'score',)
