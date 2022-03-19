from django import forms
from django.contrib.auth.models import User
import datetime
from django.forms import widgets
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

    categoryChoices = (('1', 'PC'), ('2', 'Laptop'),)

    title = forms.CharField(max_length=50)
    averageRating = forms.IntegerField(widget=widgets.HiddenInput, initial=0)
    category = forms.ChoiceField(choices=categoryChoices)
    description = forms.CharField(max_length = 200, widget=forms.Textarea(attrs={'rows':7}))

    class Meta:
        model = Post
        fields = ('title','category', 'picture','description',)

class ReviewForm(forms.ModelForm):
    comment = forms.CharField(max_length=200)
    score = forms.IntegerField(max_value=5)

    class Meta:
        model = Review
        fields = ('comment', 'score',)
