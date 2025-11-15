from django.urls import path
from dashboard import views


urlpatterns = [
    path("", views.dashboard_views, name="dashboard"),
    #  path for category
    path("das_category", views.das_category_views, name="das_category"),
    path("add_categores", views.add_categores, name="add_categores"),
    path("edit_categores/<int:pk>", views.edit_categores, name="edit_categores"),
    path("delete_categores/<int:pk>", views.delete_categores, name="delete_categores"),
    # path for POST
    path("das_post", views.das_post_views, name="das_post"),
    path("add_posts", views.add_posts, name="add_posts"),
    path("edit_post/<int:pk>", views.edit_post, name="edit_post"),
    path("delete_post/<int:pk>", views.delete_post, name="delete_post"),
    #  path for logout
    path("das_logout", views.das_logout_views, name="das_logout"),
    # path for users
    path("users/", views.users, name="users"),
    path("add_user/", views.add_user, name="add_user"),
    path("edit_user/<int:pk>", views.edit_user, name="edit_user"),
    path("delete_user/<int:pk>", views.delete_user, name="delete_user"),
]
