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

QUOTE_API = f"{API}quote/"


@dataclass
class Quote():
    """
    A class to represent a quote.
    
    Attributes
    ----------
    id (str): The id of the quote.
    dialog (str): The quote itself.
    movie (str): The id of the movie that the quote is from.
    character (str): The id of the character that said the quote.
    """
    id: str = ""
    dialog: str = ""
    movie: str = ""
    character: str = ""

def get_quote_by_id(id:str = "") -> Quote:
    """
    A function that receives a Quote id and returns a Quote object.

    Arguments
    ----------
    id (str): The id of the Quote
    """
    quote_api_id = f"{QUOTE_API}{id}"
    results = requests.get(url=quote_api_id, headers=AUTH_HEADER)
    if results.status_code == 200:
        logging.info(f"Success! You have accessed {quote_api_id}.")
        results_json = results.json()
        results_json = results_json["docs"][0]
        return Quote(
            results_json.get("id"),
            results_json.get("dialog"),
            results_json.get("movie"),
            results_json.get("character")
        )
    else:
        logging.error(f"Failed with Status Code {results_json.status_code}. Failed to get Quote from id {id}.")
        return None


def get_all_quotes(params:dict = {}) -> List:
    """
    A function that returns a list of all quotes.

    Arguments
    ----------
    params (dict): A dictionary of parameters sent in the API call.
    """
    results = requests.get(url=QUOTE_API, params=params, headers=AUTH_HEADER)
    if results.status_code == 200:
        logging.info(f"Success! You have accessed {QUOTE_API}.")
        results_json = results.json()
        quotes = []
        for quote in results_json["docs"]:
            quotes.append(
                Quote(
                    quote.get("id"),
                    quote.get("dialog"),
                    quote.get("movie"),
                    quote.get("character")
                )
            )
        # check for more pages to load
        pages = results_json["pages"]
        # if there are more than 1 page of chapters, pull the rest of the pages
        if pages > 1:
            for page in range(2,pages+1):
                addl_results = requests.get(QUOTE_API,params={"page": page}, headers=AUTH_HEADER)
                if addl_results.status_code == 200:
                    logging.info(f"Success! You have accessed {QUOTE_API} page {page}.")
                    results_json = addl_results.json()
                    for quote in results_json["docs"]:
                        quotes.append(
                            Quote(
                                quote.get("id"),
                                quote.get("dialog"),
                                quote.get("movie"),
                                quote.get("character")
                            )
                        )
                else:
                    logging.error(f"Status {addl_results.status_code}. Failed to get quotes page {page}.")
        return quotes
    else:
        logging.error(f"Status {results.status_code}. Failed to get quotes.")
        return []

def get_sorted_quotes(sort_by:str, sort_type: str) -> List:
    """
    A function that receives an argument to sort by (i.e. id, dialog, movie, character)
    and a sort type (i.e. asc: ascending, desc: descending)

    Arguments
    ----------
    sort_by (str): The Quote argument to sort by (id, dialog, movie, character)
    sort_type (str): The sort type (asc: ascending, desc: descending)
    """
    # check if correct sort_by and sort_type have been passed:
    if sort_by != "id" and sort_by != "dialog" and sort_by != "movie" and sort_by != "character":
        logging.error(f"{sort_by} is not a valid argument. Valid options: id, dialog, movie, character")
        return []
    if sort_type != "asc" and sort_type != "desc":
        logging.error(f"{sort_type} is not a valid argument. Valid options: asc, desc")
        return []

    params = {"sort": sort_by+":"+sort_type}
    results = get_all_quotes(params)
    return results

def get_quote_by_regex(quote_arg: str, regex: str) -> List:
    """
    A function that receives a Quotte argument and matches to a regex expression.

    Arguments
    ----------
    quote_arg (str): The Quote class argument to match by (i.e. id, dialog, movie, character).
    regex (str): The regex expression used to match with.
    """
    params = {quote_arg: regex}
    results = get_all_quotes(params)
    return results