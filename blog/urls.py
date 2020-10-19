from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [

    path('post/<int:pk>delete/', BlogDeleteView.as_view(), name='post_del'),
    path('post/<int:pk>edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('Post/new/', BlogCreateView.as_view(), name='post_new'),
    path('Post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),

    # All blog post entries will start with post/. Next is the primary key for our post entry
    # which will be represented as an integer <int:pk>.
    # At the url for our blog we created a primary key by using <ink:pk/id>

]
