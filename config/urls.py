from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend import views as b_views

router = routers.DefaultRouter()
# router.register(r'users', b_views.UserViewSet)

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
