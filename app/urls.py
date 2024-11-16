from django.urls import path

from . import views



urlpatterns = [
    path('',views.index),
    path('login/',views.login,name='login'),
    path('logout/',views.logouts,name='logout'),
    path('delete/',views.delete,name='delete'),
    path('details/<int:id>/',views.details,name='details'),
    path('gallery/',views.gallery,name='gallery'),
    path('register/',views.register,name='register'),
    path('profile/<int:id>/',views.profile,name='profile'),
    path('update/<int:id>/', views.update, name='update'),
]