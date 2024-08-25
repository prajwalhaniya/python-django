from django.contrib import admin
from django.urls import path, include
from .views import AuthorView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('authors/', AuthorView.as_view(), name="authors")
]