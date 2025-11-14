from django.db import models


class CarouselSlide(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='carousel/', blank=True, null=True)
    link = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class QuickLink(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    link = models.CharField(max_length=500)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class GovernmentLink(models.Model):
    name = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    url = models.URLField()
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class CompanyHistory(models.Model):
    content = models.TextField()
    year_start = models.IntegerField(default=1924)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Company History"

    def __str__(self):
        return f"Company History (since {self.year_start})"
