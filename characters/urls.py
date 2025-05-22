from django.urls import path

from characters.views import get_random_characters, CharacterListView

urlpatterns = [
    path("characters/random/", get_random_characters, name="character-random"),
    path("characters/", CharacterListView.as_view(), name="character-list"),
]

app_name = "characters"
