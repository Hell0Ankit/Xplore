from .models import Header, NavLink, FooterSection, FooterBrand


def common_data(request):
    return {
        "header_key": Header.objects.first(),
        "nav_key": NavLink.objects.all(),
        "brand": FooterBrand.objects.first(),
        "sections": FooterSection.objects.prefetch_related("links").all(),
    }
