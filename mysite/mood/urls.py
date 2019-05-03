
from django.urls import path
from . import views

urlpatterns = [
	path('', views.DiaryList.as_view(), name='diary_list'),
	path('diary/<int:pk>', views.DiaryDetail.as_view(), name='diary_detail'),
	path('create/', views.DiaryCreate.as_view(), name='diary_create'),
	path('update/<int:pk>', views.DiaryUpdate.as_view(), name='diary_update'),
	path('delete/<int:pk>', views.DearyDelete.as_view(), name='diary_delete')
]