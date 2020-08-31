from django.urls import path
from . import views
from blog.sitemaps import StaticViewSitemap ,PostSitemap
from django.contrib.sitemaps.views import sitemap
from .views import *
sitemaps = {
    'static': StaticViewSitemap,
    'post': PostSitemap
}

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:slug>/', views.category, name='category'),
    path('detail/<str:slug>/', views.post_detail, name='detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name="sitemap"),
    path('detail/<slug:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('detail/<slug:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('new-post/', views.PostCreateView.as_view(), name='new_post'),

]