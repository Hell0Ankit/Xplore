from django.urls import path
from website import views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("gallery/", views.gallery_views, name="gallery"),
    path("contact/", views.contact_views, name="contact"),
    path("terms-condition/", views.terms_views, name="terms-condition"),
]
