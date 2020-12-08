from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
import event.views
from s6 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', event.views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
