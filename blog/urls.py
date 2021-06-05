from blog.models import Post
from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$',views.views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
]