from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogs),
    path("<int:id>", views.blog)
]