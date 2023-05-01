from django.db import models
from django.contrib.auth.models import User


class Film(models.Model):
    title = models.CharField(max_length=50)
    release_year = models.PositiveSmallIntegerField()
    platform = models.CharField(max_length=20)  # Sennò una FK a un Model che ha la lista delle piattaforme disponibili

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class Review(models.Model):
    # La presenza di un record assicura che l'utente abbia visto quel film
    review_author = models.ForeignKey(User, on_delete=models.CASCADE)  # review_author
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="reviews")

    # TODO validators=[MinValueValidator(1), MaxValueValidator(5)]
    vote = models.PositiveSmallIntegerField(default=None, blank=True, null=True)
    comment = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.review_author} @ {self.film}"

    class Meta:
        ordering = ("-vote",)
