from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("user/<int:profile_id>", views.profile, name='profile'),

    # API routes
    path("posts", views.showPost, name="posts"),
    path("new-post", views.post, name="newPost")
]
