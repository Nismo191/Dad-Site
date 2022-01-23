from .models import Photo, Writing, Photo_Comment, Writing_Comment
from django import forms

class PhotoCommentForm(forms.ModelForm):
    post = forms.ModelChoiceField(queryset=Photo.objects.all())
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

    class Meta:
        model = Photo_Comment
        fields = ['name', 'body', 'post']

class WritingCommentForm(forms.ModelForm):
    post = forms.ModelChoiceField(queryset=Writing.objects.all())
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

    class Meta:
        model = Writing_Comment
        fields = ['name', 'body', 'post']