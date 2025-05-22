from django.urls import path

from characters.views import get_random_characters

urlpatterns = [
    path("characters/random/", get_random_characters, name="character-random"),
]

app_name = "characters"
