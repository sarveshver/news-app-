
from django.urls import path
from .views import home, post_comment

urlpatterns = [
    path('', home, name='home'),
    path('post_comment/<int:article_index>/', post_comment, name='post_comment'),
    
]
