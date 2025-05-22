import requests

from characters.models import Character
from rick_and_morty_api.settings import RICK_AND_MORTY_API_CHARACTERS_URL


def scrape_characters() -> list[Character]:
    next_url_to_scrape = RICK_AND_MORTY_API_CHARACTERS_URL
    # next_url_to_scrape = "https://rickandmortyapi.com/api/character"

    characters = []
    while next_url_to_scrape is not None:
        characters_response = requests.get(next_url_to_scrape).json()

        for character_dict in characters_response["results"]:
            characters.append(
                Character(
                    api_id=character_dict["id"],
                    name=character_dict["name"],
                    status=character_dict["status"],
                    species=character_dict["species"],
                    gender=character_dict["gender"],
                    image=character_dict["image"],
                )
            )
        next_url_to_scrape = characters_response["info"]["next"]

    return characters


def save_characters(characters: list[Character]) -> None:
    for character in characters:
        character.save()


def sync_characters_with_api() -> None:
    characters = scrape_characters()
    save_characters(characters)
