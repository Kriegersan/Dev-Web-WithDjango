# HelloWorld/urls.py
from django.conf.urls import url
from HelloWorld import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view()),
    url(r'^/support', views.Support.as_view()),
]
