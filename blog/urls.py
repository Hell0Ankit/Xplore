from django.urls import path
from blog import views


urlpatterns = [
    path("", views.blog_views, name="blog"),
    path("search", views.search_views, name="search"),
    path("dashboard", views.dashboard_views, name="dashboard"),
    path("<int:category_id>/", views.posts_by_category, name="posts_by_category"),
    path("<slug:blogid>", views.blog_details_views, name="blog-details"),
]
