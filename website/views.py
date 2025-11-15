from django.shortcuts import render
from blog.models import Blog, Category
from .models import (
    Hero,
    Works,
    WorkBoxex,
    Explore,
    ExploreBoxes,
    SpotsBoxes,
    Spots,
    CtaSection,
    PageTitle,
    About,
    Stats,
    CoreValuesSection,
    CoreValue,
    GalleryBreadcrumb,
    GalleryImages,
)


# Base view for app
def home_view(request):
    hero = Hero.objects.first()
    works = Works.objects.first()
    workbox = WorkBoxex.objects.all()
    explore = Explore.objects.first()
    exploreboxes = ExploreBoxes.objects.all()
    spots = Spots.objects.first()
    spotsboxes = SpotsBoxes.objects.all()
    ctasection = CtaSection.objects.first()
    posts = Blog.objects.filter(is_featured=True, status="published").order_by(
        "create_at"
    )[:3]
    categories = Category.objects.all()

    context = {
        "hero_key": hero,
        "works": works,
        "workbox": workbox,
        "explore": explore,
        "exploreboxes": exploreboxes,
        "spots": spots,
        "spotsboxes": spotsboxes,
        "ctasection": ctasection,
        "posts": posts,
        "categories": categories,
    }
    return render(request, "index.html", context)


def about_view(request):
    pagetitle = PageTitle.objects.first()
    about = About.objects.first()
    stats = Stats.objects.all()
    corevaluessection = CoreValuesSection.objects.first()
    corevalue = CoreValue.objects.all()

    context = {
        "pagetitle": pagetitle,
        "about": about,
        "stats": stats,
        "corevaluessection": corevaluessection,
        "corevalue": corevalue,
    }
    return render(request, "about.html", context)


def gallery_views(request):
    gallery_breadcrumb = GalleryBreadcrumb.objects.first()
    gallery_images = GalleryImages.objects.all()
    context = {
        "gallery_breadcrumb": gallery_breadcrumb,
        "gallery_images": gallery_images,
    }
    return render(request, "gallery.html", context)


def contact_views(request):
    return render(request, "contact.html", {})


def terms_views(request):
    return render(request, "terms-condition.html", {})
