from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from .views import redirect_view

urlpatterns = [
    path("", redirect_view),
    path("chat/", include("chat.urls")),
    path("admin/", admin.site.urls),
]
