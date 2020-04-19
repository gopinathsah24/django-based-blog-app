from django.urls import path
from . import views
from . views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns = [ path('',PostListView.as_view(),name='blog_home'),
                path('user/<str:username>',UserPostListView.as_view(),name='user_posts'),
                path('post/<int:pk>',PostDetailView.as_view(),name='post_detail'),
                path('post/new',PostCreateView.as_view(),name='post_create'),
                path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post_delete'),
                path('post/<int:pk>/update',PostUpdateView.as_view(),name='post_update'),
                path('about/',views.about,name="about_page"),
                # path('new/',views.new,name="new_page"),
                # path('new2/',views.new2,name="new_page2")
                ]