from django.urls import path

from .views import DetailUser, EditUser, RedirectUser

app_name = "users"
urlpatterns = [
    path("~redirect/", RedirectUser.as_view(), name="redirect"),
    path("~update/", EditUser.as_view(), name="update"),
    path("<str:username>/", DetailUser.as_view(), name="detail"),
]
