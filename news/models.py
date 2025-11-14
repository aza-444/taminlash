from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class NewsCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    
    class Meta:
        verbose_name_plural = "News Categories"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, unique=True, blank=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, related_name='news')
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    content = RichTextField()
    excerpt = models.TextField(max_length=500, blank=True)
    published_date = models.DateField()
    is_featured = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "News"
        ordering = ['-published_date']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to='videos/', blank=True, null=True)
    video_url = models.URLField()
    description = models.TextField(blank=True)
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title
