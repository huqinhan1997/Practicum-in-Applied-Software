"""数据库课设 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from staff import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homepage/', views.homepage),
    url(r'^homepage_staff/', views.homepage_staff),
    url(r'^homepage_manager/', views.homepage_manager),
    url(r'^club/', views.club),
    url(r'^join/', views.join),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^register_staff/', views.register_staff),
    url(r'^register_club/', views.register_club),
    url(r'^logout/', views.logout),
    url(r'^StockTrading/', views.StockTrading),
    url(r'^agree/', views.agree),
    url(r'^create_activity/', views.create_activity),
    url(r'^activity_mag/', views.activity_mag),
    url(r'^show_club/', views.show_club),
    url(r'^fabu_activity/', views.fabu_activity),
    url(r'^delete_activity/', views.delete_activity),
    url(r'^show_all_act/', views.show_all_act),
    url(r'^join_mag/', views.join_mag),
    url(r'^club_img/', views.club_img),
    url(r'^club_sum/', views.club_sum),
    url(r'^search/', views.search),
    url(r'^news/', views.news),
    url(r'^news_staff/', views.news_staff),







]
