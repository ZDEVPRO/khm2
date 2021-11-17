from django.db import models
from django.forms import TextInput, EmailInput, Textarea

from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel
from django.contrib.auth.models import User


class Teacher(models.Model):
    name = models.CharField('Ism Familya', max_length=200)
    category = models.CharField('Kasb', max_length=300)
    image = models.ImageField('Rasim', upload_to='images/')
    phone = models.CharField('Telefon raqami', max_length=100)
    whatsapp = models.CharField(blank=True, max_length=100)
    telegram = models.CharField(blank=True, max_length=100)

    class Meta:
        verbose_name = "O'qituvchilar"
        verbose_name_plural = "O'qituvchilar"

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


class News(models.Model):
    title = models.TextField('Sarlavhasi', max_length=351)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField('Tavsifi', max_length=2000)
    obshi_description = models.TextField('Hamma Tekst', blank=True, max_length=3001)
    past_description = models.TextField('Pastki Tavsif:', blank=True, max_length=1000)
    image = models.ImageField('Rasmi', upload_to='images/')
    create_on_date = models.DateField(auto_now=True)
    create_on_time = models.TimeField(auto_now=True)

    class Meta:
        verbose_name = "Yangiliklar"
        verbose_name_plural = "Yangiliklar"

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


class Total(models.Model):
    num_students = models.CharField("O'quvchilar soni", max_length=10)
    num_teachers = models.CharField("O'qituvchilar soni", max_length=10)
    num_groups = models.CharField("Guruxlar soni", max_length=10)
    num_room = models.CharField("Xonalar soni", max_length=10)

    class Meta:
        verbose_name = "Hisob"
        verbose_name_plural = "Hisob"

    def __str__(self):
        return self.num_students


class Pages(models.Model):
    title = models.CharField('Sarlavha', max_length=100)
    link = models.CharField('Link', max_length=100, blank=True)

    class Meta:
        verbose_name = "Pastki Sahifalar"
        verbose_name_plural = "Pastki Sahifalar"

    def __str__(self):
        return self.title


class AboutIndex(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Biz haqimizda (Asosiy menyu)"
        verbose_name_plural = "Biz haqimizda (Asosiy menyu)"

    def __str__(self):
        return self.title


class AboutFooter(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    phone = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    telegram = models.CharField(blank=True, max_length=100)
    whatsapp = models.CharField(blank=True, max_length=100)

    class Meta:
        verbose_name = "Biz haqimizda (Footer)"
        verbose_name_plural = "Biz haqimizda (Footer)"

    def __str__(self):
        return self.title


class ContactAboutPage(models.Model):
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.TextField(max_length=400)

    class Meta:
        verbose_name = "Aloqa malumotlari"
        verbose_name_plural = "Aloqa malumotlari"

    def __str__(self):
        return self.phone


class Logo(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logo"

    def __str__(self):
        return self.title


class Hometitle(models.Model):
    title = models.TextField(max_length=300)

    class Meta:
        verbose_name = "Sarlavha asosiy sahifa"
        verbose_name_plural = "Sarlavha asosiy sahifa"

    def __str__(self):
        return self.title


class ContactFooter(models.Model):
    phone = models.CharField(max_length=100)
    adress = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Pastki Bog'lanish"
        verbose_name_plural = "Pastki Bog'lanish"


class ContactMessage(models.Model):
    name = models.CharField('Ismi', blank=True, max_length=20)
    phone = models.CharField('Telefon raqami', blank=True, max_length=50)
    subject = models.CharField('Mavzu', blank=True, max_length=50)
    message = models.TextField('Xabar', blank=True, max_length=255)
    ip = models.CharField(blank=True, max_length=50)
    creat_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Bog'lanish bo'limi"
        verbose_name_plural = "Bog'lanish bo'limi"

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'subject', 'phone', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Name'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'phone': EmailInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Your message'}),
        }
