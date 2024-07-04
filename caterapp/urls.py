from django.urls import path
from . import views

urlpatterns = [
    path('404/', views.c404, name='404'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('book/', views.book, name='book'),
    path('contact/', views.contact, name='contact'),
    path('event/', views.event, name='event'),
    path('footer/', views.footer, name='footer'),
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial')
]
