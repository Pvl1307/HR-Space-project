from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('rh_kosmos.urls', namespace='rh_kosmos')),
                  path('', include('users.urls', namespace='users')),
                  path('', include('blog.urls', namespace='blog')),

                  path('api/', include('api.urls', namespace='api')),
                  path('', include('react.urls', namespace='react')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
