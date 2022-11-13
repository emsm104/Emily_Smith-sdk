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

MOVIE_API = f"{API}movie/"


@dataclass
class Movie():
    """
    A class to represent a movie.

    Attributes
    ----------
    id (str): The id of the movie.
    name (str): The name of the movie.
    runtimeInMinutes (int): The movie's run time in minutes.
    budgetInMillions (int): The movie's budget in millions.
    boxOfficeRevenueInMillions (int): Box office revenue in millions.
    academyAwardNominations (int): Academy Award Nominations for the movie.
    academyAwardWins (int): Academy Award wins for the movie.
    rottenTomatoesScore (int): The score on Rotten Tomatoes for the movie.
    """
    id: str = ""
    name: str = ""
    runtimeInMinutes: int = 0
    budgetInMillions: int = 0
    boxOfficeRevenueInMillions: int = 0
    academyAwardNominations: int = 0
    academyAwardWins: int = 0
    rottenTomatoesScore: float = 0


def get_all_movies(params:dict = {}) -> List:
    """
    A function that returns a list of all movies.

    Arguments
    ----------
    params (dict): A dictionary of parameters sent in the API call.
    """
    results = requests.get(url=MOVIE_API, params=params, headers=AUTH_HEADER)
    if results.status_code == 200:
        logging.info(f"Success! You have accessed {MOVIE_API}.")
        results_json = results.json()
        movies = []
        total_movies = results_json["total"]
        for i in range(total_movies):
            movie = Movie(
                id=results_json["docs"][i]["_id"],
                name=results_json["docs"][i]["name"],
                runtimeInMinutes=results_json["docs"][i]["runtimeInMinutes"],
                budgetInMillions=results_json["docs"][i]["budgetInMillions"],
                boxOfficeRevenueInMillions=results_json["docs"][i]["boxOfficeRevenueInMillions"],
                academyAwardNominations=results_json["docs"][i]["academyAwardNominations"],
                academyAwardWins=results_json["docs"][i]["academyAwardWins"],
                rottenTomatoesScore=results_json["docs"][i]["rottenTomatoesScore"]
            )
            movies.append(movie)
        return movies
    else:
        logging.error(f"Status {results.status_code}. Failed to get movies.")
        return []


def get_movie_by_id(id:str = "") -> Movie:
    """
    A function that receives a Movie id and returns a Movie object.

    Arguments
    ----------
    id (str): The id of the Movie
    """
    movie_api_id = f"{MOVIE_API}{id}"
    results = requests.get(url=movie_api_id, headers=AUTH_HEADER)
    if results.status_code == 200:
        logging.info(f"Success! You have accessed {movie_api_id}.")
        results_json = results.json()
        results_json = results_json["docs"][0]
        return Movie(
            id=results_json["_id"],
            name=results_json["name"],
            runtimeInMinutes=results_json["runtimeInMinutes"],
            budgetInMillions=results_json["budgetInMillions"],
            boxOfficeRevenueInMillions=results_json["boxOfficeRevenueInMillions"],
            academyAwardNominations=results_json["academyAwardNominations"],
            academyAwardWins=results_json["academyAwardWins"],
            rottenTomatoesScore=results_json["rottenTomatoesScore"]
        )
    else:
        logging.error(f"Failed with Status Code {results_json.status_code}. Failed to get Movie from id {id}.")
        return None


def get_movie_by_name(name:str = "") -> Movie:
    """
    A function that receives a Movie name and returns a Movie object.

    Arguments
    ----------
    name (str): The name of the Movie
    """
    results = requests.get(url=MOVIE_API, params={"name": name}, headers=AUTH_HEADER)
    if results.status_code == 200:
        logging.info(f"Success! You have accessed {MOVIE_API}.")
        results_json = results.json()
        results_json = results_json["docs"][0]
        logging.info(f"{results_json}")
        return Movie(
            id=results_json["_id"],
            name=results_json["name"],
            runtimeInMinutes=results_json["runtimeInMinutes"],
            budgetInMillions=results_json["budgetInMillions"],
            boxOfficeRevenueInMillions=results_json["boxOfficeRevenueInMillions"],
            academyAwardNominations=results_json["academyAwardNominations"],
            academyAwardWins=results_json["academyAwardWins"],
            rottenTomatoesScore=results_json["rottenTomatoesScore"]
        )
    else:
        logging.error(f"Failed with Status Code {results_json.status_code}. Failed to get Movie from {name}.")
        return None


def get_sorted_movies(sort_by:str, sort_type: str) -> List:
    """
    A function that receives an argument to sort by (i.e. _id, name, 
    runtimeInMinutes, budgetInMillions, boxOfficeRevenueInMillions, 
    academyAwardNominations, academyAwardWins, rottenTomatoesScore)
    and a sort type (i.e. asc: ascending, desc: descending)

    Arguments
    ----------
    sort_by (str): The Book argument to sort by (i.e. _id, name, 
    runtimeInMinutes, budgetInMillions, boxOfficeRevenueInMillions, 
    academyAwardNominations, academyAwardWins, rottenTomatoesScore)
    sort_type (str): The sort type (asc: ascending, desc: descending)
    """
    # check if correct sort_by and sort_type have been passed:
    if sort_by != "_id" and sort_by != "name" and sort_by != "runtimeInMinutes" and sort_by != "budgetInMillions" and sort_by != "academyAwardNominations" and sort_by != "academyAwardWins" and sort_by != "rottenTomatoesScore":
        logging.error(f"{sort_by} is not a valid argument. Valid options: _id, name, runtimeInMinutes, budgetInMillions, boxOfficeRevenueInMillions, academyAwardNominations, academyAwardWins, rottenTomatoesScore")
        return []
    if sort_type != "asc" and sort_type != "desc":
        logging.error(f"{sort_type} is not a valid argument. Valid options: asc, desc")
        return []

    params = {"sort": sort_by+":"+sort_type}
    logging.info(params)
    results = get_all_movies(params)
    return results


def get_movie_by_regex(movie_arg: str, regex: str) -> List:
    """
    A function that receives a Movie argument and matches to a regex expression.

    Arguments
    ----------
    movie_arg (str): The Movie class argument to match by (i.e. _id, name, 
    runtimeInMinutes, budgetInMillions, boxOfficeRevenueInMillions, 
    academyAwardNominations, academyAwardWins, rottenTomatoesScore).
    regex (str): The regex expression used to match with.
    """
    params = {movie_arg: regex}
    results = get_all_movies(params)
    return results