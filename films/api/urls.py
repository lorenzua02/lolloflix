from django.urls import path, include
from films.api.views import UserViewSet, FilmViewSet, ReviewCreateAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"user", UserViewSet, basename="cazzoequa")
router.register(r"film", FilmViewSet, basename="film")

urlpatterns = [
    path("film/<int:film_pk>/review/", ReviewCreateAPIView.as_view(), name="film-review"),
    path("", include(router.urls)),
]
