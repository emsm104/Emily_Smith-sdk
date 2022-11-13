import unittest
import os
import sys
from chapters import (
    Chapter,
    get_chapter_by_id,
    get_chapter_by_name,
    get_chapter_by_regex,
    get_sorted_chapters,
    get_all_chapters
)


class TestChapters(unittest.TestCase):
    """
    Testing suite for chapters.py.
    """
    def test_chapter_class(self):
        """
        Test the creation of a Chapter class.
        """
        chapter = Chapter()
        self.assertEqual(chapter.id,"")
        self.assertEqual(chapter.chapterName,"")
        self.assertEqual(chapter.book,"")

    def test_get_chapter_by_id(self):
        """
        Test get_chapter_by_id().
        """
        chapter_by_id = get_chapter_by_id("6091b6d6d58360f988133b8b")
        self.assertEqual(chapter_by_id.id, "6091b6d6d58360f988133b8b")
        self.assertEqual(chapter_by_id.chapterName, "A Long-expected Party")
        self.assertEqual(chapter_by_id.book, "5cf5805fb53e011a64671582")

    def test_get_chapter_by_name(self):
        """
        Test get_chapter_by_name().
        """
        chapter_by_name = get_chapter_by_name("A Long-expected Party")
        self.assertEqual(chapter_by_name.id, "6091b6d6d58360f988133b8b")
        self.assertEqual(chapter_by_name.chapterName, "A Long-expected Party")
        self.assertEqual(chapter_by_name.book, "5cf5805fb53e011a64671582")

    def test_get_all_chapters(self):
        """
        Test get_all_chapters().
        """
        test_chapters = get_all_chapters()
        self.assertEqual(len(test_chapters), 62)

    def test_get_sorted_chapters_asc(self):
        """
        Test get_sorted_chapters().
        """
        test_asc_chapters = get_sorted_chapters("_id","asc")
        self.assertEqual(test_asc_chapters[0].id, "6091b6d6d58360f988133b8b")
        self.assertEqual(test_asc_chapters[0].chapterName, "A Long-expected Party")
        self.assertEqual(test_asc_chapters[0].book, "5cf5805fb53e011a64671582")

    def test_get_sorted_chapters_desc(self):
        """
        Test get_sorted_chapters().
        """
        test_desc_chapters = get_sorted_chapters("_id","desc")
        self.assertEqual(test_desc_chapters[0].id, "6091b6d6d58360f988133bc8")
        self.assertEqual(test_desc_chapters[0].chapterName, "The Grey Havens")
        self.assertEqual(test_desc_chapters[0].book, "5cf58080b53e011a64671584")

    def test_get_chapters_regex(self):
        """
        Test get_chapter_by_regex(). 
        """
        test_chapters = get_chapter_by_regex("chapterName", "/Party/i")
        self.assertIn("Party",test_chapters[0].chapterName)


if __name__ == "__main__":
    unittest.main()
    