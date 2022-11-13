from dataclasses import dataclass
from typing import List
import requests
import logging

# Set up logging
logging.basicConfig(
    format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    filename='lotr_sdk.log',
    level=logging.INFO
    )

# Import api and header
try:
    from settings import API, AUTH_HEADER
except ImportError as e:
    logging.exception(e)

CHARACTER_API = f"{API}character/"


@dataclass
class Character():
    """
    A class to represent a character.

    Attributes
    ----------
    id (str): The id of the character.
    height (str): The height of the character.
    race (str): The race of the character.
    gender (str): The gender of the character.
    birth (str): The birthdate of the character.
    spouse (str): The spouse of the character.
    death (str): The date of death for the character.
    realm (str): The realm the character belongs to.
    hair (str): The kind of hair that the character has.
    wikiUrl (url): The Wiki url of the character.
    """
    id: str = ""
    height: str = ""
    race: str = ""
    gender: str = ""
    birth: str = ""
    spouse: str = ""
    death: str = ""
    realm: str = ""
    hair: str = ""
    name: str = ""
    wikiUrl: str = ""


def get_all_characters(params:dict = {}) -> List:
    """
    A function that returns a list of all characters.

    Arguments
    ----------
    params (dict): A dictionary of parameters sent in the API call.
    """
    results = requests.get(url=CHARACTER_API, params=params, headers=AUTH_HEADER)
    if results.status_code == 200:
        logging.info(f"Success! You have accessed {CHARACTER_API}.")
        results_json = results.json()
        characters = []
        total_characters = results_json["total"]
        for i in range(total_characters):
            # at least one of the characters doesn't have a gender
            try:
                gender_char = results_json["docs"][i]["gender"]
            except:
                gender_char = ""
            char = Character(
                id=results_json["docs"][i]["_id"],
                height=results_json["docs"][i]["height"],
                race=results_json["docs"][i]["race"],
                gender=gender_char, 
                birth=results_json["docs"][i]["birth"],
                spouse=results_json["docs"][i]["spouse"],
                death=results_json["docs"][i]["death"],
                realm=results_json["docs"][i]["realm"],
                hair=results_json["docs"][i]["hair"],
                name=results_json["docs"][i]["name"]
            )
            characters.append(char)
        return characters
    else:
        logging.error(f"Status {results.status_code}. Failed to get characters.")
        return []


def get_character_by_id(id:str = "") -> Character:
    """
    A function that receives a Character id and returns a Character object.

    Arguments
    ----------
    id (str): The id of the Character
    """
    char_api_id = f"{CHARACTER_API}{id}"
    results = requests.get(url=char_api_id, headers=AUTH_HEADER)
    if results.status_code == 200:
        logging.info(f"Success! You have accessed {char_api_id}.")
        results_json = results.json()
        results_json = results_json["docs"][0]
        # at least one of the characters doesn't have a gender
        try:
            gender_char = results_json["gender"]
        except:
            gender_char = ""
        return Character(
            id=results_json["_id"],
            height=results_json["height"],
            race=results_json["race"],
            gender=gender_char, 
            birth=results_json["birth"],
            spouse=results_json["spouse"],
            death=results_json["death"],
            realm=results_json["realm"],
            hair=results_json["hair"],
            name=results_json["name"]
        )
    else:
        logging.error(f"Failed with Status Code {results_json.status_code}. Failed to get Character from id {id}.")
        return None


def get_character_by_name(name:str = "") -> Character:
    """
    A function that receives a Character name and returns a Character object.

    Arguments
    ----------
    name (str): The name of the Character
    """
    results = requests.get(url=CHARACTER_API, params={"name": name}, headers=AUTH_HEADER)
    if results.status_code == 200:
        logging.info(f"Success! You have accessed {CHARACTER_API}.")
        results_json = results.json()
        results_json = results_json["docs"][0]
        # at least one of the characters doesn't have a gender
        try:
            gender_char = results_json["gender"]
        except:
            gender_char = ""
        return Character(
            id=results_json["_id"],
            height=results_json["height"],
            race=results_json["race"],
            gender=gender_char, 
            birth=results_json["birth"],
            spouse=results_json["spouse"],
            death=results_json["death"],
            realm=results_json["realm"],
            hair=results_json["hair"],
            name=results_json["name"]
        )
    else:
        logging.error(f"Failed with Status Code {results_json.status_code}. Failed to get Character from {name}.")
        return None


def get_sorted_characters(sort_by:str, sort_type: str) -> List:
    """
    A function that receives an argument to sort by (i.e. id, height,
    race, gender, birth, spouse, death, realm, hair, name) and a 
    sort type (i.e. asc: ascending, desc: descending)

    Arguments
    ----------
    sort_by (str): The Character argument to sort by (i.e. id, height,
    race, gender, birth, spouse, death, realm, hair, name)
    sort_type (str): The sort type (asc: ascending, desc: descending)
    """
    # check if correct sort_by and sort_type have been passed:
    if sort_by != "_id" and sort_by != "height" and sort_by != "race" and sort_by != "gender" and sort_by != "birth" and sort_by != "spouse" and sort_by != "death" and sort_by != "realm" and sort_by != "hair" and sort_by != "name":
        logging.error(f"{sort_by} is not a valid argument. Valid options: _id, height, race, gender, birth, spouse, death, realm, hair, name")
        return []
    if sort_type != "asc" and sort_type != "desc":
        logging.error(f"{sort_type} is not a valid argument. Valid options: asc, desc")
        return []

    params = {"sort": sort_by+":"+sort_type}
    logging.info(params)
    results = get_all_characters(params)
    return results


def get_character_by_regex(char_arg: str, regex: str) -> List:
    """
    A function that receives a Character argument and matches to a regex expression.

    Arguments
    ----------
    char_arg (str): The Character class argument to match by (i.e. id, height,
    race, gender, birth, spouse, death, realm, hair, name).
    regex (str): The regex expression used to match with.
    """
    params = {char_arg: regex}
    results = get_all_characters(params)
    return results