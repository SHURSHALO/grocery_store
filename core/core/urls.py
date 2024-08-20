from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('products/', include('products.urls', namespace='products')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
