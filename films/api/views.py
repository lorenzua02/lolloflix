from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, mixins, generics
from rest_framework.exceptions import ValidationError

from films.api.pagination import SmallSetPagination
from films.api.serializers import UserSerializer, FilmSerializer, ReviewSerializer
from films.models import Film, Review
from django.contrib.auth.models import User


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = SmallSetPagination


class FilmViewSet(ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()

    filter_backends = [SearchFilter]
    search_fields = ["platform"]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        film_pk = self.kwargs.get("film_pk")
        film = get_object_or_404(Film, pk=film_pk)

        review_author = self.request.user
        review_queryset = Review.objects.filter(film=film, review_author=review_author)
        if review_queryset.exists():
            # Potrebbe essere prima "visto", poi "recensione". Se c'è già, elimino la vecchia TODO PUT?
            review_queryset.delete()
            # raise ValidationError("You Have Already Reviewed this film!")
        serializer.save(film=film, review_author=review_author)
