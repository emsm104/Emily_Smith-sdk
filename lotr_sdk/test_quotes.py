import unittest
import os
import sys
from quotes import (
    Quote,
    get_quote_by_id,
    get_all_quotes,
    get_sorted_quotes,
    get_quote_by_regex
)


class TestQuotes(unittest.TestCase):
    """
    Testing suite for quotes.py.
    """
    def test_quote_class(self):
        """
        Test the creation of a Quote class.
        """
        quote = Quote()
        self.assertEqual(quote.id,"")
        self.assertEqual(quote.dialog,"")
        self.assertEqual(quote.movie,"")
        self.assertEqual(quote.character,"")

    def test_get_quote_by_id(self):
        """
        Test get_quote_by_id().
        """
        quote = get_quote_by_id("5cd96e05de30eff6ebccebe3")
        self.assertEqual(quote.id, "5cd96e05de30eff6ebccebe3")
        self.assertEqual(quote.dialog, "By all that you hold dear on this good earth, I bid you stand! Men of the West!")
        self.assertEqual(quote.movie, "5cd95395de30eff6ebccde5d")
        self.assertEqual(quote.character, "5cd99d4bde30eff6ebccfbe6")

    def test_get_all_quotes(self):
        """
        Test get_all_quotes().
        """
        test_quotes = get_all_quotes()
        self.assertEqual(len(test_quotes), 2390)

    def test_get_sorted_quotes_asc(self):
        """
        Test get_sorted_quotes().
        """
        test_asc_chapters = get_sorted_quotes("character","asc")
        self.assertEqual(test_asc_chapters[0].id, "5cd96e05de30eff6ebcced20")
        self.assertEqual(test_asc_chapters[0].dialog, "Gondor calls for aid.")
        self.assertEqual(test_asc_chapters[0].movie, "5cd95395de30eff6ebccde5d")
        self.assertEqual(test_asc_chapters[0].character, "5cd99d4bde30eff6ebccfbe6")

    def test_get_sorted_quotes_desc(self):
        """
        Test get_sorted_quotes().
        """
        test_desc_chapters = get_sorted_quotes("character","desc")
        self.assertEqual(test_desc_chapters[0].id, "5cd96e05de30eff6ebccedc6")
        self.assertEqual(test_desc_chapters[0].dialog, "Yes, Mama.")
        self.assertEqual(test_desc_chapters[0].movie, "5cd95395de30eff6ebccde5b")
        self.assertEqual(test_desc_chapters[0].character, "5cdbe73516d496d2c2940848")

    def test_get_quotes_regex(self):
        """
        Test get_quote_by_regex(). 
        """
        test_quotes = get_quote_by_regex("dialog", "/Mama/i")
        self.assertIn("Mama",test_quotes[0].dialog)

if __name__ == "__main__":
    unittest.main()
