from dataclasses import dataclass, field
from typing import List
from chapters import Chapter
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

BOOK_API = f"{API}book/"


@dataclass
class Book():
    """
    A class to represent a book.

    Attributes
    ----------
    id (str): The id of the book.
    name (str): The name of the book.
    chapters (list): A list of chapters from the book.
    """
    id: str = ""
    name: str = ""
    chapters: List[str] = field(default_factory=list)


def get_all_books(params:dict = {}) -> List:
    """
    A function that returns a list of all books.

    Arguments
    ----------
    params (dict): A dictionary of parameters sent in the API call.
    """
    results = requests.get(url=BOOK_API, params=params, headers=AUTH_HEADER)
    if results.status_code == 200:
        logging.info(f"Success! You have accessed {BOOK_API}.")
        results_json = results.json()
        books = []
        total_books = results_json["total"]
        for i in range(total_books):
            book = Book(
                id=results_json["docs"][i]["_id"],
                name=results_json["docs"][i]["name"]
            )
            books.append(book)
        return books
    else:
        logging.error(f"Status {results.status_code}. Failed to get books.")
        return []


def get_book_by_id(id:str = "") -> Book:
    """
    A function that receives a Book id and returns a Book object.

    Arguments
    ----------
    id (str): The id of the Book
    """
    book_api_id = f"{BOOK_API}{id}"
    results = requests.get(url=book_api_id, headers=AUTH_HEADER)
    if results.status_code == 200:
        logging.info(f"Success! You have accessed {book_api_id}.")
        results_json = results.json()
        results_json = results_json["docs"][0]
        return Book(
            results_json.get("_id"),
            results_json.get("name"),
            results_json.get("chapters")
        )
    else:
        logging.error(f"Failed with Status Code {results_json.status_code}. Failed to get Chapter from id {id}.")
        return None


def get_chapters_by_book_id(id: str = "") -> List:
    """
    A function that receives a Book id and returns a list of Chapters
    from the book.

    Arguments
    ----------
    id (str): The id of the Book
    """
    book_chapters_api = f"{BOOK_API}{id}/chapter"
    results = requests.get(url=book_chapters_api, headers=AUTH_HEADER)
    if results.status_code == 200:
        logging.info(f"Success Status {results.status_code}! You have accessed {book_chapters_api}.")
        chapters = []
        results_json = results.json()
        total_chapters = results_json["total"]
        for chapter in results_json["docs"]:
            chapters.append(
                            Chapter(
                                chapter.get("_id"),
                                chapter.get("chapterName")
                            )
                        )
            # logging.info(f'{chapter}')
        logging.info(f"Success! You have accessed {total_chapters} chapters at {book_chapters_api}.")
        return chapters
    else:
        logging.error(f"Status {results.status_code}. Failed to get chapters for {book_chapters_api}.")
        return []


def get_book_by_name(name:str = "") -> Book:
    """
    A function that receives a Book name and returns a Book object.

    Arguments
    ----------
    name (str): The name of the Book
    """
    results = requests.get(url=BOOK_API, params={"name": name}, headers=AUTH_HEADER)
    if results.status_code == 200:
        logging.info(f"Success! You have accessed {BOOK_API}.")
        results_json = results.json()
        results_json = results_json["docs"][0]
        return Book(
            results_json.get("_id"),
            results_json.get("name"),
            results_json.get("chapters")
        )
    else:
        logging.error(f"Failed with Status Code {results_json.status_code}. Failed to get Book from {name}.")
        return None


def get_sorted_books(sort_by:str, sort_type: str) -> List:
    """
    A function that receives an argument to sort by (i.e. _id, name)
    and a sort type (i.e. asc: ascending, desc: descending)

    Arguments
    ----------
    sort_by (str): The Book argument to sort by (_id, name)
    sort_type (str): The sort type (asc: ascending, desc: descending)
    """
    # check if correct sort_by and sort_type have been passed:
    if sort_by != "_id" and sort_by != "name":
        logging.error(f"{sort_by} is not a valid argument. Valid options: _id, name")
        return []
    if sort_type != "asc" and sort_type != "desc":
        logging.error(f"{sort_type} is not a valid argument. Valid options: asc, desc")
        return []

    params = {"sort": sort_by+":"+sort_type}
    logging.info(params)
    results = get_all_books(params)
    return results



def get_book_by_regex(book_arg: str, regex: str) -> List:
    """
    A function that receives a Book argument and matches to a regex expression.

    Arguments
    ----------
    book_arg (str): The Book class argument to match by (i.e. id, name).
    regex (str): The regex expression used to match with.
    """
    params = {book_arg: regex}
    results = get_all_books(params)
    return results