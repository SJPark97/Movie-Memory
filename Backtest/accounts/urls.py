from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [
    path('myprofile/', views.my_profile),
    path('genres_movies/', views.genres_movies),
    path('<int:user_id>/profile/', views.user_profile),
    path('<int:user_id>/profile/follow/', views.follow),
]
