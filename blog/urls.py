from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts.views import index, blog, post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('post/', post, name='post'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



