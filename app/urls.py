from django.urls import path

from . import views

urlpatterns = [
    path('',views.home.as_view()),
    path('login/',views.login_user,name="login_user"),
    path('logout/',views.logout_user,name="logout_user"),
    path('register/',views.register,name="register"),
    path('create_post/',views.create_post,name="create_post"),
]