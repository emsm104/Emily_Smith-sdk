# What is emily_smith-SDK?
Emily_Smith-SDK is an SDK for [The One API](https://the-one-api.dev). The One API is an open-source API for Lord of The Rings data. 
Data for books, chapters, characters, movies, and quotes are available.

# Prerequisites
In order to authenticate your API calls, create a token here: [https://the-one-api.dev/sign-up](https://the-one-api.dev/sign-up)

# Compatibility
Your project needs to use a Python version of 3.9.10 or later.

# Install the package
To install, use `pip`:
> pip install emily_smith-sdk

# Logs
Logs will be captured in the lotr_sdk.log file.

# How to Use: Characters Example
To return all characters:
```python
from lotr_sdk import characters
print(characters.get_all_characters())
```
To return a characters by the id:
```python
from lotr_sdk import characters
print(characters.get_character_by_id("5cd99d4bde30eff6ebccfbbf"))
```
To return characters by their name:
```python
from lotr_sdk import characters
print(characters.get_character_by_name("Adrahil I"))
```
To return a sorted list of characters (id ascending):
```python
from lotr_sdk import characters
print(characters.get_sorted_characters("_id","asc"))
```
To return a sorted list of characters (id descending):
```python
from lotr_sdk import characters
print(characters.get_sorted_characters("_id","desc"))
```
To regex search for a character by attribute:
```python
from lotr_sdk import characters
print(characters.get_character_by_regex("name", "/Belem/i"))
```

## Books:
```python
# a Book object
Book(id: str, name: str, chapters: [Chapter])
get_all_books(params={})
# return a Book object from an id
get_book_by_id(id="")
# return a list of Chapter objects from a Book id
get_chapters_by_book_id(id="")
# return a Book object from a name
get_book_by_name(name="")
# return a list of sorted Books
# can be sorted by any Book attribute either ascending or descending
get_sorted_books(sort_by="", sort_type="")
# return a Book object from a regex expression
get_book_by_regex(book_arg="", regex="")
```

## Chapters:
```python
# a Chapter object
Chapter(id: str, chapterName: str, book: str)
# return a list of all Chapter objects
get_all_chapters(params={})
# return a Chapter object from an id
get_chapter_by_id(id="")
# return a Chapter object from a name
get_chapter_by_name(name="")
# return a list of sorted Chapters
# can be sorted by any Chapter attribute either ascending or descending
get_sorted_books(sort_by="", sort_type="")
# return a Chapter object from a regex expression
get_chapter_by_regex(chapter_arg="", regex="")
```

## Characters:
```python
# a Character object
Character(id: str, height: str, race: str, gender: str, birth: str, spouse: str, death: str, realm: str, hair: str, name: str, wikiUrl: str)
# return a list of all Character objects
get_all_characters(params={})
# return a Character object from an id
get_character_by_id(id="")
# return a Character object from a name
get_character_by_name(name="")
# return a list of sorted Characters
# can be sorted by any Character attribute either ascending or descending
get_sorted_characters(sort_by="", sort_type="")
# return a Character object from a regex expression
get_character_by_regex(char_arg="", regex="")
```

## Movies:
```python
# a Movie object
Movie(id: str, name: str, runtimeInMinutes: int, budgetInMillions: int, boxOfficeRevenueInMillions: int, academyAwardNominations: int, academyAwardWins: int, rottenTomatoesScore: float)
# return a list of all Movie objects
get_all_movies(params={})
# return a Movie object from an id
get_movie_by_id(id="")
# return a Movie object from a name
get_movie_by_name(name="")
# return a list of sorted Movies
# can be sorted by any Movie attribute either ascending or descending
get_sorted_movies(sort_by="", sort_type="")
# return a Movie object from a regex expression
get_movie_by_regex(char_arg="", regex="")
```

## Quotes:
```python
# a Movie object
Quote(id: str, dialog: str, movie: str, character: str)
# return a list of all Quote objects
get_all_quotes(params={})
# return a Quote object from an id
get_quote_by_id(id="")
# return a Quote object from a name
get_quote_by_name(name="")
# return a list of sorted Quotes
# can be sorted by any Quote attribute either ascending or descending
get_sorted_quotes(sort_by="", sort_type="")
# return a Quote object from a regex expression
get_quote_by_regex(char_arg="", regex="")
```
