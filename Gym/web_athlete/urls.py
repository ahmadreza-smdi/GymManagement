from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.main,name="home"),
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^dashboard/$',views.dashboard)
]
