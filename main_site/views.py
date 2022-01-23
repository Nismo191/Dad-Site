import random

from django.shortcuts import render

from .models import Photo, Writing, Tag, Photo_Comment, Writing_Comment
from .forms import PhotoCommentForm, WritingCommentForm

def index(request):
    photos = Photo.objects.all()
    writings = Writing.objects.all()
    tags = Tag.objects.all()

    num_photos = Photo.objects.all().count()
    num_writings = Writing.objects.all().count()
    num_tags = Tag.objects.all().count()

    photo_list = list(Photo.objects.all())
    rand_img = random.choice(photo_list)

    context = {
        'photos': photos,
        'writings': writings,
        'tags': tags,
        'num_photos': num_photos,
        'num_writings': num_writings,
        'num_tags': num_tags,
        'rand_img': rand_img
    }
    return render(request, 'index.html', context=context)



def photo(request):
    photos = Photo.objects.filter(published=True)

    if request.method == 'POST':
        comment_form = PhotoCommentForm(data=request.POST)
        print('POST')
        if comment_form.is_valid():
            print('valid')
            comment_form.save()

    else:
        comment_form = PhotoCommentForm()

    context = {
        'photos': photos,
        'comment_form': comment_form
    }
    return render(request, 'photography.html', context=context)



def writing(request):
    writings = Writing.objects.all()

    if request.method == 'POST':
        comment_form = WritingCommentForm(data=request.POST)
        print('POST')
        if comment_form.is_valid():
            print('valid')
            comment_form.save()

    else:
        comment_form = WritingCommentForm()

    context = {
        'writings': writings,
        'comment_form': comment_form
    }
    return render(request, 'writing.html', context=context)