
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from core.views import maintenance_page, locked_page
from userauths import views
from dashboard import views
from course import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('userauths/', include('userauths.urls')),
    path('contactus/', include('contactapp.urls')),
    path('webdevelopment/', include('course.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('maintenance/', maintenance_page, name='maintenance'),
    # path('locked/', locked_page, name='locked'),
    # path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)