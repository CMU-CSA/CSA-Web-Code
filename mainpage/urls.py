from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^aboutus/', views.aboutus, name='aboutus'),
    url(r'^activities', views.activities, name='activities'),
    url(r'^login', views.login, name="login"),
]

