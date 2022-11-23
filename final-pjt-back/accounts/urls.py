from django.urls import path
from . import views


urlpatterns = [
    path('myprofile/', views.my_profile),
    path('genres_movies/', views.genres_movies),
    path('new_kind_movies/', views.new_kind_movies),
    path('my_notice/', views.my_notice),
    path('<int:notice_id>/change_notice/', views.change_notice),
    path('<int:user_id>/profile/', views.user_profile),
    path('<int:user_id>/profile/follow/', views.follow),
]
