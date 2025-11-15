from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Blog, Category
from django.db.models import Q


# Create your views here.
def blog_views(request):
    all_blogs = Blog.objects.all().order_by("-id")
    return render(request, "blog.html", {"all_blogs": all_blogs})


def blog_details_views(request, blogid):
    blog_details = get_object_or_404(Blog, slug=blogid, status="published")
    context = {
        "blog_details": blog_details,
    }
    return render(request, "blog-details.html", context)


def dashboard_views(request):
    return render(request, "dashboard.html", {})


def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status="published", category=category_id)

    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     return redirect("home")

    category = get_object_or_404(Category, pk=category_id)

    context = {"posts": posts, "category": category}
    return render(request, "posts_by_category.html", context)


def search_views(request):
    keyword = request.GET.get("keyword")
    print(keyword)
    blogs = Blog.objects.filter(title__icontains=keyword)  # simple serach query
    blogs = Blog.objects.filter(
        Q(title__icontains=keyword)
        | Q(short_description__icontains=keyword)
        | Q(blog_body__icontains=keyword),
        status="published",
    )  # using Q object complex query
    contex = {"blogs": blogs, "keyword": keyword}
    return render(request, "search.html", contex)
