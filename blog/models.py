from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class Tag(models.Model):
    ''' Table for Tags'''
    title = models.CharField(max_length=50)
    url = models.SlugField(unique=True, max_length=50)

    def get_absolute_url(self):
        pass
        # return reverse('', kwargs={'url': self.u
        # rl})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        db_table = 'tag'
        ordering = ['title']


class Category(models.Model):
    ''' Table for Categories'''
    title = models.CharField(max_length=50)
    url = models.SlugField(unique=True, max_length=50)

    def get_absolute_url(self):
        pass
        # return reverse('', kwargs={'url': self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = 'category'
        ordering = ['title']


class Post(models.Model):
    '''Table for Posts'''
    title = models.CharField(max_length=150)
    url = models.SlugField(unique=True, max_length=50)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='author', null=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    photo = models.ImageField(max_length=150, upload_to='photos/%Y/%m/%d/', blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='tags')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    draft = models.BooleanField(default=False)

    def get_absolute_url(self):
        pass
        # return reverse('', kwargs={'url': self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        db_table = 'post'
        ordering = ['-updated_date']


class Review(models.Model):
    ''' Table for Review'''
    user_name = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='user', null=True)
    comment = models.TextField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        db_table = 'review'