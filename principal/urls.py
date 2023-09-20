
from django.contrib import admin
from django.urls import path
from principal.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
]
