from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='home'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('contact', views.contact, name='contact'),
    path('news/add', views.CreateNewsView.as_view(), name='news_add'),
    path('news/<int:pk>/update', views.UpdateNewsView.as_view(), name='news_update'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name='news_delete'),
    path('user/<str:username>', views.UserAllNewsView.as_view(), name='user_news'),
]
