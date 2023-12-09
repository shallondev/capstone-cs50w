from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('create_exam/', views.create_exam, name='create_exam'),
    path('take_exam/int:exam_id/', views.take_exam, name='take_exam'),
]