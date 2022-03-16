from django.urls import path
from rerig import views

app_name = 'rerig'

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('login/', views.user_login, name="login"),
path('register/', views.register, name="register"),
path('account/<slug:username_slug>/', views.account, name="account"),
path('search/', views.search, name="search"),
path('add_post/', views.add_post, name="add_post"),
path('logout/', views.user_logout, name='logout'),
path('post/<int:post_id>', views.show_post, name="show_post"),
]
