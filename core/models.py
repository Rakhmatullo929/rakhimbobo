from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'News'

class Partner(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='partners/')
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']

class TeamMember(models.Model):
    POSITION_CHOICES = [
        ('CEO', 'CEO'),
        ('CTO', 'CTO'),
        ('CFO', 'CFO'),
        ('COO', 'COO'),
        ('Manager', 'Manager'),
        ('Specialist', 'Specialist'),
        ('Other', 'Other'),
    ]
    
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team/')
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.position}"

    class Meta:
        ordering = ['order', 'name']

class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    map_coordinates = models.CharField(max_length=200, blank=True, null=True)
    working_hours = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return "Contact Information"

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    is_new = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
