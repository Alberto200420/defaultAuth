from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/", include("djoser.urls")),
    path("api/", include("apps.users.urls")),
    path('admin/', admin.site.urls),
]
