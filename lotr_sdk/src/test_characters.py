import unittest
import os
import sys
from characters import (
    Character,
    get_all_characters,
    get_character_by_id,
    get_character_by_name,
    get_sorted_characters,
    get_character_by_regex
)


class TestCharacters(unittest.TestCase):
    """
    Testing suite for characters.py.
    """
    def test_character_class(self):
        """
        Test the creation of a Character class.
        """
        character = Character()
        self.assertEqual(character.id,"")
        self.assertEqual(character.height,"")
        self.assertEqual(character.race,"")
        self.assertEqual(character.gender,"")
        self.assertEqual(character.birth,"")
        self.assertEqual(character.spouse,"")
        self.assertEqual(character.death,"")
        self.assertEqual(character.realm,"")
        self.assertEqual(character.hair,"")
        self.assertEqual(character.name,"")

    def test_get_all_characters(self):
        """
        Test get_all_characters().
        """
        test_characters = get_all_characters()
        self.assertEqual(len(test_characters), 933)

    def test_get_character_by_id(self):
        """
        Test get_character_by_id().
        """
        char_by_id = get_character_by_id("5cd99d4bde30eff6ebccfbbf")
        self.assertEqual(char_by_id.id, "5cd99d4bde30eff6ebccfbbf")
        self.assertEqual(char_by_id.height, "")
        self.assertEqual(char_by_id.race, "Human")
        self.assertEqual(char_by_id.gender, "Male")
        self.assertEqual(char_by_id.birth, "Before ,TA 1944")
        self.assertEqual(char_by_id.spouse, "")
        self.assertEqual(char_by_id.death, "Late ,Third Age")
        self.assertEqual(char_by_id.realm, "")
        self.assertEqual(char_by_id.hair, "")
        self.assertEqual(char_by_id.name, "Adrahil I")

    def test_get_character_by_name(self):
        """
        Test get_character_by_name().
        """
        char_by_name = get_character_by_name("Adrahil I")
        self.assertEqual(char_by_name.id, "5cd99d4bde30eff6ebccfbbf")
        self.assertEqual(char_by_name.height, "")
        self.assertEqual(char_by_name.race, "Human")
        self.assertEqual(char_by_name.gender, "Male")
        self.assertEqual(char_by_name.birth, "Before ,TA 1944")
        self.assertEqual(char_by_name.spouse, "")
        self.assertEqual(char_by_name.death, "Late ,Third Age")
        self.assertEqual(char_by_name.realm, "")
        self.assertEqual(char_by_name.hair, "")
        self.assertEqual(char_by_name.name, "Adrahil I")

    def test_get_sorted_chars_asc(self):
        """
        Test get_sorted_characters().
        """
        test_asc_chars = get_sorted_characters("_id","asc")
        self.assertEqual(test_asc_chars[0].id, "5cd99d4bde30eff6ebccfbbe")
        self.assertEqual(test_asc_chars[0].height, "")
        self.assertEqual(test_asc_chars[0].race, "Human")
        self.assertEqual(test_asc_chars[0].gender, "Female")
        self.assertEqual(test_asc_chars[0].birth, "")
        self.assertEqual(test_asc_chars[0].spouse, "Belemir")
        self.assertEqual(test_asc_chars[0].death, "")
        self.assertEqual(test_asc_chars[0].realm, "")
        self.assertEqual(test_asc_chars[0].hair, "")
        self.assertEqual(test_asc_chars[0].name, "Adanel")

    def test_get_sorted_chars_desc(self):
        """
        Test get_sorted_characters().
        """
        test_asc_chars = get_sorted_characters("_id","desc")
        self.assertEqual(test_asc_chars[0].id, "5cdbe73516d496d2c2940848")
        self.assertEqual(test_asc_chars[0].height, "")
        self.assertEqual(test_asc_chars[0].race, "Human")
        self.assertEqual(test_asc_chars[0].gender, "Male")
        self.assertEqual(test_asc_chars[0].birth, "")
        self.assertEqual(test_asc_chars[0].spouse, "")
        self.assertEqual(test_asc_chars[0].death, "")
        self.assertEqual(test_asc_chars[0].realm, "Rohan")
        self.assertEqual(test_asc_chars[0].hair, "")
        self.assertEqual(test_asc_chars[0].name, "Éothain")

    def test_get_characters_by_regex(self):
        """
        Test get_characters_by_regex(). 
        """
        test_books = get_character_by_regex("name", "/Belem/i")
        self.assertIn("Belem",test_books[0].name)

if __name__ == "__main__":
    unittest.main()
