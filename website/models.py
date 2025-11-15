from django.db import models
from blog.models import Category


class NavLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Header(models.Model):
    logo_text = models.CharField(max_length=100, default="Xplore")
    url = models.URLField(max_length=200)

    show_login = models.BooleanField(default=True)
    show_signup = models.BooleanField(default=True)

    def __str__(self):
        return self.logo_text


class Hero(models.Model):
    hero_heading = models.CharField(max_length=50)
    sub_para = models.CharField(max_length=200)
    button_text = models.CharField(max_length=200)
    button_text_2 = models.CharField(max_length=200)

    def __str__(self):
        return self.hero_heading


class Works(models.Model):
    main_heading = models.CharField(max_length=50)
    sub_para = models.CharField(max_length=100)
    button_text = models.CharField(max_length=200)

    def __str__(self):
        return self.main_heading


class WorkBoxex(models.Model):
    icon_class = models.CharField(
        max_length=100, help_text="Enter icon class e.g. fa fa-home or bi bi-house"
    )
    box_heading = models.CharField(max_length=50)
    box_para = models.CharField(max_length=200)

    def __str__(self):
        return self.box_heading


class Explore(models.Model):
    main_heading = models.CharField(max_length=50)
    sub_para = models.CharField(max_length=100)

    def __str__(self):
        return self.main_heading


class ExploreBoxes(models.Model):
    icon_class = models.CharField(
        max_length=100, help_text="Enter icon class e.g. fa fa-home or bi bi-house"
    )
    box_heading = models.CharField(max_length=50)
    box_para = models.CharField(max_length=200)

    def __str__(self):
        return self.box_heading


class Spots(models.Model):
    main_heading = models.CharField(max_length=50)
    sub_para = models.CharField(max_length=100)

    def __str__(self):
        return self.main_heading


class SpotsBoxes(models.Model):
    # image = models.ImageField(upload_to=media, height_field=None, width_field=None, max_length=None)
    box_heading = models.CharField(max_length=50)
    box_para = models.CharField(max_length=200)

    def __str__(self):
        return self.box_heading


class CtaSection(models.Model):
    main_heading = models.CharField(max_length=50)
    sub_para = models.CharField(max_length=100)
    child_heading = models.CharField(max_length=50)
    child_para = models.CharField(max_length=200)
    button_url = models.URLField(max_length=200)
    button_text = models.CharField(max_length=200)

    def __str__(self):
        return self.main_heading


# Footer main section (like Explore, Company, Support)
class FooterSection(models.Model):
    title = models.CharField(max_length=100)  # Example: "Explore", "Company"

    def __str__(self):
        return self.title


# Links under each section
class FooterLink(models.Model):
    section = models.ForeignKey(
        FooterSection, on_delete=models.CASCADE, related_name="links"
    )
    name = models.CharField(max_length=100)  # Example: "Local Shops", "About Us"
    url = models.URLField(max_length=300)

    def __str__(self):
        return f"{self.name} ({self.section.title})"


# Brand info (like Xplore left side text)
class FooterBrand(models.Model):
    brand_name = models.CharField(max_length=100, default="Xplore")
    description = models.TextField(
        blank=True, null=True
    )  # Example: "Discover hidden spots ..."
    year = models.IntegerField(default=2025)
    tagline = models.CharField(
        max_length=255, blank=True, null=True
    )  # Example: "Made with  for local discovery"

    def __str__(self):
        return self.brand_name


# About Us models here


class PageTitle(models.Model):
    title = models.CharField(max_length=50)
    para = models.TextField()

    def __str__(self):
        return self.title


class About(models.Model):
    short_heading = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    para = models.TextField()
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.title


class Stats(models.Model):
    icon_class = models.CharField(
        max_length=100,
        help_text="Enter icon class e.g. fa fa-home or bi bi-house",
        default="fas fa-map-pin",
    )
    stats_num = models.CharField(max_length=50)
    title = models.CharField(max_length=50, default="Our Core Values")

    def __str__(self):
        return self.title


class CoreValuesSection(models.Model):
    short_heading = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class CoreValue(models.Model):
    icon_class = models.CharField(
        max_length=100, help_text="Enter icon class e.g. fa fa-home or bi bi-house"
    )
    title = models.CharField(max_length=50)
    para = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class GalleryBreadcrumb(models.Model):
    title = models.CharField(max_length=50)
    para = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class GalleryImages(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="upload/%y/%m/%d")
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.title
