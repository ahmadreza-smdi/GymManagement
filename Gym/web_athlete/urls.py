from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.main,name="home"),
    url(r'^login/$',views.loginn),
    url(r'^registerations/$',views.register),
    url(r'^dashboard/$',views.dashboard),
    url(r'^dashboard/time/$',views.choose_time),
    url(r'^dashboard/settings/$',views.settings),
    url(r'^dashboard/logout/$',views.logout_view),

]
