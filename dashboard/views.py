from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Blog, Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BlogPostForm, AddUserform, EditUserForm
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your views here.


@login_required(login_url="login")
def dashboard_views(request):
    category_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()
    active_users = User.objects.filter(is_active=True)

    context = {
        "category_count": category_count,
        "blog_count": blog_count,
        "active_users": active_users,
    }

    return render(request, "dashboard/dashboard.html", context)


@login_required(login_url="login")
def das_category_views(request):
    category = Category.objects.all()
    context = {
        "category": category,
    }

    return render(request, "dashboard/das_category.html", context)


@login_required(login_url="login")
def das_post_views(request):
    blog = Blog.objects.all()
    context = {
        "blog": blog,
    }

    return render(request, "dashboard/das_post.html", context)


def das_logout_views(request):

    return render(request, "dashboard/das_logout.html")


@login_required(login_url="login")
def add_categores(request):
    if request.method == "POST":
        category_name = request.POST.get("category_name")
        if category_name:
            Category.objects.create(category_name=category_name)
            return redirect("das_category")
    newcat = Category.objects.all().order_by("-id")
    context = {newcat: "newcat"}

    return render(request, "dashboard/add_categores.html", context)


@login_required(login_url="login")
def edit_categores(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        new_name = request.POST.get("category_name")
        category.category_name = new_name
        category.save()
        return redirect("das_category")
    return render(request, "dashboard/edit_categores.html", {"category": category})


@login_required(login_url="login")
def delete_categores(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect("das_category")


@login_required(login_url="login")
def add_posts(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.slug = slugify(blog.title)
            blog.save()
            return redirect("blog")
    else:
        form = BlogPostForm()
    return render(request, "dashboard/add_posts.html", {"form": form})


@login_required(login_url="login")
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("das_post")  # ya jahan redirect karna ho
    else:
        form = BlogPostForm(instance=post)

    return render(request, "dashboard/edit_post.html", {"form": form})


@login_required(login_url="login")
def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect("das_post")


@login_required(login_url="login")
def users(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "dashboard/users.html", context)


@login_required(login_url="login")
def add_user(request):
    if request.method == "POST":
        form = AddUserform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users")
    form = AddUserform()
    context = {"form": form}
    return render(request, "dashboard/add_user.html", context)


@login_required(login_url="login")
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("users")
    form = EditUserForm(instance=user)

    context = {"form": form, "user": user}
    return render(request, "dashboard/edit_user.html", context)


@login_required(login_url="login")
def delete_user(request, pk):
    post = get_object_or_404(User, pk=pk)
    post.delete()
    return redirect("users")
