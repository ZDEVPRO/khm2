from home.models import Total, Pages, ContactFooter, AboutIndex, AboutFooter, Logo, ContactAboutPage, Hometitle


def total(request):
    total_latest = Total.objects.all().order_by('-id')[:1]
    context = {
        'total_latest': total_latest,
    }
    return context


def pages(request):
    pages_slider = Pages.objects.all().order_by('id')[:7]
    context = {
        'pages_slider': pages_slider,
    }
    return context


def contact_footer(request):
    contact_slider = ContactFooter.objects.all().order_by('id')[:1]
    context = {
        'contact_slider': contact_slider,
    }
    return context


def about_index(request):
    about_index_slider = AboutIndex.objects.all().order_by('id')[:1]
    context = {
        'about_index_slider': about_index_slider,
    }
    return context


def about_footer(request):
    about_footer_slider = AboutFooter.objects.all().order_by('id')[:1]
    context = {
        'about_footer_slider': about_footer_slider,
    }
    return context


def contact_about_page(request):
    contact_about = ContactAboutPage.objects.all().order_by('id')[:1]
    context = {
        'contact_about': contact_about,
    }
    return context


def logo(request):
    logo_index = Logo.objects.all().order_by('id')[:1]
    context = {
        'logo_index': logo_index,
    }
    return context


def hometitle(request):
    home_title = Hometitle.objects.all().order_by('id')[:1]
    context = {
        'home_title': home_title,
    }
    return context
