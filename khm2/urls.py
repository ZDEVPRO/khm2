from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('contact/', views.contactus, name='contactus'),
    path('news/<int:id>/<slug:slug>', views.news_detail, name='news_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "home.views.handle_not_found"
