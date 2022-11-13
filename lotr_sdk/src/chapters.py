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

CHAPTER_API = f"{API}chapter/"


@dataclass
class Chapter():
    """
    A class to represent a chapter.
    
    Attributes
    ----------
    id (str): The id of the chapter.
    chapterName (str): The name of the chapter.
    book (str): The id of the book that the chapter belongs to.
    """
    id: str = ""
    chapterName: str = ""
    book: str = ""


def get_chapter_by_id(id:str = "") -> Chapter:
    """
    A function that receives a Chapter id and returns a Chapter object.

    Arguments
    ----------
    id (str): The id of the Chapter
    """
    chapter_api_id = CHAPTER_API+id 
    results = requests.get(url=chapter_api_id, headers=AUTH_HEADER)
    if results.status_code == 200:
        logging.info(f"Success! You have accessed {chapter_api_id}.")
        results_json = results.json()
        results_json = results_json["docs"][0]
        return Chapter(
            results_json.get("_id"),
            results_json.get("chapterName"),
            results_json.get("book")
        )
    else:
        logging.error(f"Failed with Status Code {results_json.status_code}. Failed to get Chapter from id {id}.")
        return None


def get_chapter_by_name(name:str = "") -> Chapter:
    """
    A function that receives a name (chapterName) and returns a Chapter object.

    Arguments
    ----------
    name (str): The chapterName of the Chapter
    """
    results = requests.get(url=CHAPTER_API, params={"chapterName": name}, headers=AUTH_HEADER)
    if results.status_code == 200:
        logging.info(f"Success! You have accessed {CHAPTER_API}.")
        results_json = results.json()
        results_json = results_json["docs"][0]
        return Chapter(
            results_json.get("_id"),
            results_json.get("chapterName"),
            results_json.get("book")
        )
    else:
        logging.error(f"Failed with Status Code {results_json.status_code}. Failed to get Chapter from chapterName {name}.")
        return None


def get_all_chapters(params:dict = {}) -> List:
    """
    A function that returns a list of all chapters.

    Arguments
    ----------
    params (dict): A dictionary of parameters sent in the API call.
    """
    results = requests.get(url=CHAPTER_API, params=params, headers=AUTH_HEADER)
    if results.status_code == 200:
        logging.info(f"Success! You have accessed {CHAPTER_API}.")
        results_json = results.json()
        chapters = []
        for chapter in results_json["docs"]:
            chapters.append(
                Chapter(
                    chapter.get("_id"),
                    chapter.get("chapterName"),
                    chapter.get("book")
                )
            )
        # check for more pages to load
        pages = results_json["pages"]
        # if there are more than 1 page of chapters, pull the rest of the pages
        if pages > 1:
            for page in range(2,pages+1):
                addl_results = requests.get(CHAPTER_API,params={"page": page}, headers=AUTH_HEADER)
                if addl_results.status_code == 200:
                    logging.info(f"Success! You have accessed {CHAPTER_API} page {page}.")
                    results_json = addl_results.json()
                    for chapter in results_json["docs"]:
                        chapters.append(
                            Chapter(
                                chapter.get("_id"),
                                chapter.get("chapterName"),
                                chapter.get("book")
                            )
                        )
                else:
                    logging.error(f"Status {addl_results.status_code}. Failed to get chapters page {page}.")
        return chapters
    else:
        logging.error(f"Status {results.status_code}. Failed to get chapters.")
        return []


def get_sorted_chapters(sort_by:str, sort_type: str) -> List:
    """
    A function that receives an argument to sort by (i.e. _id, chapterName, book)
    and a sort type (i.e. asc: ascending, desc: descending)

    Arguments
    ----------
    sort_by (str): The Chapter argument to sort by (_id, chapterName, book)
    sort_type (str): The sort type (asc: ascending, desc: descending)
    """
    # check if correct sort_by and sort_type have been passed:
    if sort_by != "_id" and sort_by != "chapterName" and sort_by != "book":
        logging.error(f"{sort_by} is not a valid argument. Valid options: _id, chapterName, book")
        return []
    if sort_type != "asc" and sort_type != "desc":
        logging.error(f"{sort_type} is not a valid argument. Valid options: asc, desc")
        return []

    params = {"sort": sort_by+":"+sort_type}
    results = get_all_chapters(params)
    return results


def get_chapter_by_regex(chapter_arg: str, regex: str) -> List:
    """
    A function that receives a Chapter argument and matches to a regex expression.

    Arguments
    ----------
    chapter_arg (str): The Chapter class argument to match by (i.e. id, chapterName, book).
    regex (str): The regex expression used to match with.
    """
    params = {chapter_arg: regex}
    results = get_all_chapters(params)
    return results

