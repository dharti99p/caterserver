"""
URL configuration for caterserver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from caterapp import views

router = routers.DefaultRouter()
# index
router.register(r'heros', views.HeroViewSet)
# about
router.register(r'about', views.AboutViewSet)
router.register(r'descabout', views.DescAboutViewSet)
router.register(r'chefabout', views.ChefAboutViewSet)
router.register(r'countabout', views.CountAboutViewSet)
# blog
router.register(r'blog', views.BlogViewSet)
# book
router.register(r'book', views.BookViewSet)
# contact
router.register(r'contact', views.ContactViewSet)
# event
router.register(r'event', views.EventViewSet)
router.register(r'wedding', views.WeddingViewSet)
router.register(r'corporate', views.CorporateViewSet)
router.register(r'cocktail', views.CocktailViewSet)
router.register(r'buffet', views.BuffetViewSet)
# footer
router.register(r'footeritem', views.FooterItemViewSet)
# menu
router.register(r'starter', views.MenuStarterViewSet)
router.register(r'menumain', views.MenuMainViewSet)
router.register(r'drinksmenu', views.MenuDrinksViewSet)
router.register(r'offersmenu', views.MenuOffersViewSet)
router.register(r'specialmenu', views.MenuSpecialViewSet)
# service_menu
router.register(r'service', views.ServiceViewSet)
router.register(r'servicecustomer', views.ServiceCustomersViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("caterapp.urls"), name='caterapp'),
    path('api/', include(router.urls))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)