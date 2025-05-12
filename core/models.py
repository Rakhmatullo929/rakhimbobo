from django.db import models
from django.utils import timezone
from django.utils.text import slugify



class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name='Ссылка')
    content = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='articles/', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name='Ссылка')
    content = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Partner(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    logo = models.ImageField(upload_to='partners/', verbose_name='Логотип')
    website = models.URLField(blank=True, null=True, verbose_name='Сайт')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

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
    
    name = models.CharField(max_length=200, verbose_name='Имя')
    position = models.CharField(max_length=100, choices=POSITION_CHOICES, verbose_name='Должность')
    bio = models.TextField(verbose_name='Биография')
    photo = models.ImageField(upload_to='team/', verbose_name='Фотография')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')

    def __str__(self):
        return f"{self.name} - {self.position}"

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class Contact(models.Model):
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    map_coordinates = models.CharField(max_length=200, blank=True, null=True, verbose_name='Координаты карты')
    working_hours = models.CharField(max_length=200, blank=True, null=True, verbose_name='Рабочие часы')

    def __str__(self):
        return "Contact Information"
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class ContactMessage(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=255, verbose_name='Тема')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name='Ссылка')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение')
    is_new = models.BooleanField(default=False, verbose_name='Новинка')
    is_available = models.BooleanField(default=True, verbose_name='Доступность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_at']
