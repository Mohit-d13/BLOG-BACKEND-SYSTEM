from django.urls import path
from .views import create, update, delete

app_name = "blog"

urlpatterns = [
    path("create/", create, name="create"),
    path("<int:pk>/update/", update, name="update"),
    path("<int:pk>/delete/", delete, name="delete")
]
