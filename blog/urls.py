
from django.urls import path
from . import views

from .views import HomeView, ArticleView, AddView, UpdateView, DeleteView, AddCategoryView, CategoryView, LikeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView, AddComment


urlpatterns = [
 #path ('',views.home,name="home"),
 path('',HomeView.as_view(),name="home"),
 path('article/<int:pk>',ArticleView.as_view(),name="article_details"),
 path('add_post',AddView.as_view(),name="add_post"),
 path('add_category',AddCategoryView.as_view(),name="add_category"),
 path('article/edit/<int:pk>',UpdateView.as_view(),name="update_post"),
 path('article/<int:pk>/remove',DeleteView.as_view(),name="delete_post"),
 path('register',views.register,name="register"),
 path('login',views.login,name="login"),
 path('logout', views.logout, name="logout"),
 path('category/<str:cats>',CategoryView,name="category"),
 path('like/<int:pk>',LikeView,name="like_post"),
 path('edit_profile/<int:id>',views.edit_profile,name="edit_profile"),
 path('profile/<int:pk>',ShowProfilePageView.as_view(),name="user_profile"),
 path('profile_page/<int:pk>',EditProfilePageView.as_view(),name="edit_profile_page"),
 path('create_profile_page',CreateProfilePageView.as_view(),name="create_profile_page"),
 path('article/<int:pk>/comment',AddComment.as_view(),name="add_comment"),
 path('search',views.search,name="search-bar"),
 path('postComment',views.postComment,name="postComment"),



]