import unittest
import os
import sys
from books import (
    Book,
    get_all_books,
    get_book_by_id,
    get_chapters_by_book_id,
    get_book_by_name,
    get_book_by_regex,
    get_sorted_books
)


class TestBooks(unittest.TestCase):
    """
    Testing suite for books.py.
    """
    def test_book_class(self):
        """
        Test the creation of a Book class.
        """
        book = Book()
        self.assertEqual(book.id,"")
        self.assertEqual(book.name,"")
        self.assertEqual(book.chapters,[])

    def test_get_all_books(self):
        """
        Test get_all_books().
        """
        test_books = get_all_books()
        self.assertEqual(len(test_books), 3)

    def test_get_book_by_id(self):
        """
        Test get_book_by_id().
        """
        book_by_id = get_book_by_id("5cf5805fb53e011a64671582")
        self.assertEqual(book_by_id.id, "5cf5805fb53e011a64671582")
        self.assertEqual(book_by_id.name, "The Fellowship Of The Ring")

    def test_get_chapters_by_book_id(self):
        """
        Test get_chapters_by_book_id().
        """
        list_of_chapters = get_chapters_by_book_id("5cf5805fb53e011a64671582")
        self.assertEqual(len(list_of_chapters), 22)
        self.assertEqual(list_of_chapters[0].id, "6091b6d6d58360f988133b8b")

    def test_get_book_by_name(self):
        """
        Test get_book_by_name().
        """
        book_by_name = get_book_by_name("The Two Towers")
        self.assertEqual(book_by_name.id, "5cf58077b53e011a64671583")
        self.assertEqual(book_by_name.name, "The Two Towers")

    def test_get_sorted_books_asc(self):
        """
        Test get_sorted_chapters().
        """
        test_asc_books = get_sorted_books("_id","asc")
        self.assertEqual(test_asc_books[0].id, "5cf5805fb53e011a64671582")
        self.assertEqual(test_asc_books[0].name, "The Fellowship Of The Ring")

    def test_get_sorted_books_desc(self):
        """
        Test get_sorted_chapters().
        """
        test_desc_books = get_sorted_books("_id","desc")
        self.assertEqual(test_desc_books[0].id, "5cf58080b53e011a64671584")
        self.assertEqual(test_desc_books[0].name, "The Return Of The King")

    def test_get_books_regex(self):
        """
        Test get_book_by_regex(). 
        """
        test_books = get_book_by_regex("name", "/Fellowship/i")
        self.assertIn("Fellowship",test_books[0].name)

    
if __name__ == "__main__":
    unittest.main()

    