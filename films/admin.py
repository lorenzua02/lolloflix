from django.contrib import admin

from films.models import Film, Review


admin.site.register(Review)
admin.site.register(Film)
