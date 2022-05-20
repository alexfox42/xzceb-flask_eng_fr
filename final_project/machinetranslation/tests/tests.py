import unittest

from translator import french_to_english, english_to_french

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        with self.assertRaisesRegex(ValueError, 'text must be provided'):
             english_to_french(None)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        with self.assertRaisesRegex(ValueError, 'text must be provided'):
             french_to_english(None)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


unittest.main()