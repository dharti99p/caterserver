from email.mime import image
from operator import mod
from django.db import models
from django.forms import CharField, ImageField

# Create your models here.


# index_models
class Hero(models.Model):
    image = models.ImageField(upload_to='hero/')

# about models
class About(models.Model):
    image = models.ImageField(upload_to=('About'))


class DescAbout(models.Model):
    description = models.CharField(max_length=100)


class ChefAbout(models.Model):
    image = models.ImageField(upload_to=('About'))
    chef_name = models.CharField(max_length=50)
    chef_type = models.CharField(max_length=50)


class CountAbout(models.Model):
    numbers = models.IntegerField()
    count_name = models.CharField(max_length=50)


# blogmodels
class Blog(models.Model):
    image = models.ImageField(upload_to=('Blog'))
    date = models.IntegerField()
    month = models.CharField(max_length=20)
    test = models.CharField(max_length=50)


# bookmodels
class Booking(models.Model):
    image = models.ImageField(upload_to=('book'))


# contactmodels
class Contact(models.Model):
    address = models.CharField(max_length=100)
    email1 = models.EmailField()
    email2 = models.EmailField()
    phone1 = models.CharField(max_length=50)
    phone2 = models.CharField(max_length=50)


# event_models
class Event(models.Model):
    image = models.ImageField(upload_to=('Event'))
    imgtype = models.CharField(max_length=50)


class Wedding(models.Model):
    image = models.ImageField(upload_to=('Event'))
    imgtype = models.CharField(max_length=50)


class Corporate(models.Model):
    image = models.ImageField(upload_to=('Event'))
    imgtype = models.CharField(max_length=50)


class Cocktail(models.Model):
    image = models.ImageField(upload_to=('Event'))
    imgtype = models.CharField(max_length=50)


class Buffet(models.Model):
    image = models.ImageField(upload_to=('Event'))
    imgtype = models.CharField(max_length=50)


# footer_models
class FooterItem(models.Model):
    item_name = models.CharField(max_length=50)


# menu_models
class MenuStarter(models.Model):
    image = models.ImageField(upload_to=('Menu'))
    food_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)


class MenuMain(models.Model):
    image = models.ImageField(upload_to='Menu/')
    food_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)


class MenuDrinks(models.Model):
    image = models.ImageField(upload_to='Menu/')
    food_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)


class MenuOffers(models.Model):
    image = models.ImageField(upload_to='Menu/')
    food_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)


class MenuSpecial(models.Model):
    image = models.ImageField(upload_to='Menu/')
    food_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)


# service_models
class Service(models.Model):
    icon = models.CharField(max_length=50)
    service_name = models.CharField(max_length=50)
    service_desc = models.CharField(max_length=100)


class ServiceCustomers(models.Model):
    image = models.ImageField(upload_to='Service/')
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    review = models.TextField()