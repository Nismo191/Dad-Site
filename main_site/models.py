from django.db import models
from django.utils.html import mark_safe
from .image_processing import make_thumbnail

class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=750)
    tag = models.ManyToManyField('Tag')
    published = models.BooleanField(default=True)
    published_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        ordering = ['published_date']

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)

        make_thumbnail(self.thumbnail, self.image, (500, 500), 'thumb')

        super(Photo, self).save(*args, **kwargs)

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
        return ""

    def get_tag(self):
        return "\n".join([tag.tag for tag in self.tag.all()])

    def get_tag_id(self):
        return "\n".join([str(tag.id) for tag in self.tag.all()])
    
    def __str__(self):
        return self.title

class Writing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    tag = models.ManyToManyField('Tag')
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['published_date']

    def __str__(self):
        return self.title


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Photo_Comment(models.Model):
    post = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Writing_Comment(models.Model):
    post = models.ForeignKey(Writing, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)