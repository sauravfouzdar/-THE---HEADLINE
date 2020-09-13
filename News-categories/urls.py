from django.conf.urls import url
from . import views


urlpatterns = [

   url(r'^panel/category/category-list/$', views.category_list, name='category_list'),
   url(r'^panel/category/add-category/$', views.add_category, name='add_category'),
]