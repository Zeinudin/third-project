from django.urls import path

from .views import *
from . import views

urlpatterns = [
		path('', post_list),
		path('', quote_list),
		path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
		path('post/new/', views.post_new, name='post_new'),
		path('post/<int:pk>/', views.post_detail, name='post_detail')
]