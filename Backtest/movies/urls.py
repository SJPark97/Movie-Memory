from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/genres/<int:genres_pk>/', views.genres_movies, name = 'genre_recommend'),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/reviews/', views.review_create),
    path('movies/<int:movie_pk>/likes/', views.movies_like),
    path('movies/<int:user_pk>/like_movies/', views.like_movies),
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('reviews/<int:user_pk>/like_reviews/', views.like_reviews),
    path('reviews/<int:review_pk>/comments/', views.comment_create),
    path('reviews/<int:review_pk>/likes/', views.reviews_like),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('comments/<int:comment_pk>/likes/', views.comments_like),
    path('user/<int:user_pk>/reviews/', views.user_reviews),
    path('user/<int:user_pk>/comments/', views.user_comments),
    # # 필수 작성
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    path(
        'swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'
    ),
]
