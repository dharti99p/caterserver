from django.contrib import admin
from .models import *

# Register your models here.


# admin_admin
@admin.register(Hero)
class HeroImage(admin.ModelAdmin):
    list_display = ['image']

# About Admin
@admin.register(About)
class AboutImage(admin.ModelAdmin):
    list_display = ['image']


@admin.register(DescAbout)
class DescInfo(admin.ModelAdmin):
    list_display = ['description']


@admin.register(ChefAbout)
class ChefInfo(admin.ModelAdmin):
    list_display = ['image', 'chef_name', 'chef_type']


@admin.register(CountAbout)
class CountInfo(admin.ModelAdmin):
    list_display = ['numbers', 'count_name']
    
    
# blogadmin
@admin.register(Blog)
class BlogInfo(admin.ModelAdmin):
    list_display = ['image', 'date', 'month', 'test']


# bookadmin
@admin.register(Booking)
class BookForm(admin.ModelAdmin):
    list_display = ['image']


# Contactadmin
@admin.register(Contact)
class ContactInfo(admin.ModelAdmin):
    list_display = ['address', 'email1', 'email2', 'phone1', 'phone2']


# event_admin
@admin.register(Event)
class AllEvent(admin.ModelAdmin):
    list_display = ['image', 'imgtype']


@admin.register(Wedding)
class WeddingEvent(admin.ModelAdmin):
    list_display = ['image', 'imgtype']


@admin.register(Corporate)
class CorporateEvent(admin.ModelAdmin):
    list_display = ['image', 'imgtype']


@admin.register(Cocktail)
class CocktailEvent(admin.ModelAdmin):
    list_display = ['image', 'imgtype']


@admin.register(Buffet)
class BuffetEvent(admin.ModelAdmin):
    list_display = ['image', 'imgtype']


# footer_admin
@admin.register(FooterItem)
class ItemInfo(admin.ModelAdmin):
    list_display = ['item_name']


# menu_admin
@admin.register(MenuStarter)
class Starter(admin.ModelAdmin):
    list_display = ['image', 'food_name', 'price', 'food_desc']


@admin.register(MenuMain)
class MainCourse(admin.ModelAdmin):
    list_display = ['image', 'food_name', 'price', 'food_desc']


@admin.register(MenuDrinks)
class Drinks(admin.ModelAdmin):
    list_display = ['image', 'food_name', 'price', 'food_desc']

    
@admin.register(MenuOffers)
class Offers(admin.ModelAdmin):
    list_display = ['image', 'food_name', 'price', 'food_desc']


@admin.register(MenuSpecial)
class Special(admin.ModelAdmin):
    list_display = ['image', 'food_name', 'price', 'food_desc']


# service_admin
@admin.register(Service)
class ServiceInfo(admin.ModelAdmin):
    list_display = ['icon', 'service_name', 'service_desc']


@admin.register(ServiceCustomers)
class CustomersInfo(admin.ModelAdmin):
    list_display = ['image', 'name', 'profession', 'review']






# name = admin
# otp = admin@123