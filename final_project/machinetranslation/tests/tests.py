import unittest
from translator import english_to_french

class testengfrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('hello'), 'bonjour') #test when hello is given as input then bonjour is output
        self.assertEqual(english_to_french('Null'),'Nulle') # test when null is given as input

from translator import french_to_english

class testfrenglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('bonjour'), 'hello') #test when bonjour is given as input hello is output
        self.assertEqual(french_to_english('Nulle'),'Null') #test when null is given as input 
unittest.main()
