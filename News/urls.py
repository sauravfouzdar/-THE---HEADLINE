from django.conf.urls import url

from . import views


urlpatterns = [
    
     url(r'^news/(?P<pk>\d+)/$', views.body_of_news, name='body_of_news'),
     url(r'^panel/news/list/$', views.news_list, name='news_list'),
     url(r'^panel/news/add/$', views.add_news, name='add_news'),
     url(r'^panel/news/delete/(?P<pk>\d+)/$', views.delete_news, name='delete_news'),

]






