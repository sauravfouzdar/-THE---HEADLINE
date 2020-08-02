from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^business/$', views.business, name='business'),
    url(r'^sports/$', views.sports, name='sports'),
    url(r'^science/$', views.science, name='science'),
]
