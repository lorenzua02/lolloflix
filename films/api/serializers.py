from rest_framework import serializers

from films.models import Review, Film
from django.contrib.auth.models import User


class ReviewSerializer(serializers.ModelSerializer):
    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ("film",)


class FilmSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        logged_user = self.context['request'].user
        if not logged_user.is_anonymous:
            linked_review = Review.objects.filter(film=instance, review_author=logged_user)
            representation['seen'] = linked_review.exists()

        if len(representation['reviews']) != 0:
            reviews = [x['vote'] for x in representation['reviews']]  # TODO not djangotonic way :/
            representation['avg_vote'] = sum(reviews) / len(reviews)

        return representation

    class Meta:
        model = Film
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    films = serializers.SerializerMethodField()

    def get_films(self, instance):
        # return FilmSerializer(instance.films, many=True).data
        seen = Review.objects.filter(review_author_id=instance.id)
        return ReviewSerializer(seen, many=True).data

    class Meta:
        model = User
        # fields = "__all__"
        fields = ("id", "username", "films")
