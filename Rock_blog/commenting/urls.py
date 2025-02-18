from django.urls import path
from .views import detail, reply

app_name = "commenting"

urlpatterns = [
    path("<int:post_id>/comment/", detail, name="detail"),
    path("<int:comment_id>/reply/", reply, name="reply")
]
