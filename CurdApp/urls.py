from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog_list', views.blog_list, name='blog_list'),
    path('blog_detail/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('blog_delete/<int:blog_id>', views.blog_delete, name='blog_delete'),
    path('blog_update/<int:blog_id>/', views.blog_update, name='blog_update'),

]