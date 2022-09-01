from django.urls import path
from blog.views import HomePosts

urlpatterns = [
    path('', HomePosts.as_view(), name='home'),
]
