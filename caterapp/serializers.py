
from rest_framework import serializers
from .models import *


# index_serializer
class HeroSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ['id', 'image']


# about_serializer
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'image']


class DescAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescAbout
        fields = ['id', 'description']


class ChefAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChefAbout
        fields = ['id', 'image', 'chef_name', 'chef_type']


class CountAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountAbout
        fields = ['id', 'numbers', 'count_name']


# blog_serializer
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'image', 'date', 'month', 'test']


# book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'image']


# contact
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'address', 'email1', 'email2', 'phone1', 'phone2']


# event
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'image', 'imgtype']


class WeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wedding
        fields = ['id', 'image', 'imgtype']


class CorporateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporate
        fields = ['id', 'image', 'imgtype']


class CocktailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = ['id', 'image', 'imgtype']


class BuffetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buffet
        fields = ['id', 'image', 'imgtype']


# footer
class FooterItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterItem
        fields = ['id', 'item_name']


# menu
class MenuStarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuStarter
        fields = ['id', 'image', 'food_name', 'price', 'food_desc']


class MenuMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuMain
        fields = ['id', 'image', 'food_name', 'price', 'food_desc']


class MenuDrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuDrinks
        fields = ['id', 'image', 'food_name', 'price', 'food_desc']


class MenuOffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuOffers
        fields = ['id', 'image', 'food_name', 'price', 'food_desc']


class MenuSpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuSpecial
        fields = ['id', 'image', 'food_name', 'price', 'food_desc']


# service_admin
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'icon', 'service_name', 'service_desc']

    
class ServiceCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCustomers
        fields = ['id', 'image', 'name', 'profession', 'review']