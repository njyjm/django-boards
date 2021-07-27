from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.BoardListView.as_view(), name='home'),
    # path('<int:pk>/', views.board_topics, name='board_topics'),
    path('<int:pk>/', views.TopicListView.as_view(), name='board_topics'),
    path('<int:pk>/new/', views.new_topic, name='new_topic'),
    # path('<int:pk>/topics/<int:topic_pk>/', views.topic_posts, name='topic_posts'),
    path('<int:pk>/topics/<int:topic_pk>/', views.PostListView.as_view(), name='topic_posts'),
    path('<int:pk>/topics/<int:topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    # path('new_post/', views.new_post, name='new_post'),
    # path('new_post/', views.NewPostView.as_view(), name='new_post'),
    path('<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/', 
        views.PostUpdateView.as_view(), name='edit_post'),
]
