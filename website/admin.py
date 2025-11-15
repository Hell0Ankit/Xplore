from django.contrib import admin
from .models import (
    Header,
    NavLink,
    Hero,
    Works,
    WorkBoxex,
    Explore,
    ExploreBoxes,
    SpotsBoxes,
    Spots,
    CtaSection,
    FooterBrand,
    FooterSection,
    FooterLink,
    PageTitle,
    About,
    Stats,
    CoreValuesSection,
    CoreValue,
    GalleryImages,
    GalleryBreadcrumb,
)

# Register your models here.
admin.site.register(Header)
admin.site.register(NavLink)
admin.site.register(Hero)
admin.site.register(Works)
admin.site.register(WorkBoxex)
admin.site.register(Explore)
admin.site.register(ExploreBoxes)
admin.site.register(Spots)
admin.site.register(SpotsBoxes)
admin.site.register(CtaSection)
admin.site.register(FooterBrand)
admin.site.register(FooterSection)
admin.site.register(FooterLink)
admin.site.register(PageTitle)
admin.site.register(About)
admin.site.register(Stats)
admin.site.register(CoreValuesSection)
admin.site.register(CoreValue)
admin.site.register(GalleryBreadcrumb)
admin.site.register(GalleryImages)
