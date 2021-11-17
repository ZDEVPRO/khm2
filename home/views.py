from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Teacher, ContactForm, ContactMessage, News, Total

from django.http import Http404
from django.shortcuts import render
from home.models import Teacher


def handle_not_found(request, exception):
    return render(request, '404_page/base.html')


def index(request):
    teachers_latest = Teacher.objects.all().order_by('-id')[:3]
    page = "home"
    context = {'page': page,
               'teacher_latest': teachers_latest,
               }
    return render(request, 'index/base.html', context)


def total(request):
    total_latest = Total.objects.all().order_by('-id')[:1]
    context = {
        'total_latest': total_latest,
    }
    return render(request, 'components/total.html', context)


def news(request):
    news_latest = News.objects.all().order_by('-id')[:20]
    # page = "home"
    context = {
        'news_latest': news_latest,
    }
    return render(request, 'news/base.html', context)


def news_detail(request, id, slug):
    news_latest = News.objects.all().order_by('-id')[:8]
    news = News.objects.get(pk=id)
    context = {
        'news': news,
        'product_latest': news_latest,
    }
    return render(request, 'news_detail/base.html', context)


def about(request):
    return render(request, 'about/base.html')


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Sizning xabaringiz qabul qilindi! Rahmat')
            return HttpResponseRedirect('/')
    form = ContactForm
    context = {'form': form, }
    return render(request, 'contact/base.html', context)
