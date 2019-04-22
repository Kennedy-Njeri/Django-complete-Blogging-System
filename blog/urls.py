from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import index, blog, post, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('post/<id>', post, name='post-detail'),
    path('tinymce/', include('tinymce.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



