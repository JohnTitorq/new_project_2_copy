from django.urls import path
from .views import index, top_sellers, register, profile, advertisement_post, login, advertisement, advertisement_post


urlpatterns=[
    path("", index, name="main-page"),
    path("top-sellers/", top_sellers, name="top-sellers"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("profile/", profile, name="profile"),
    path("advertisement-post/", advertisement_post, name="advertisement-post"),
    path("advertisement/", advertisement, name="advertisement")
]