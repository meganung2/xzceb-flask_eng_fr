import unittest

from translator import frenchtoEnglish, englishToFrench

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchtoEnglish("Bonjour"), {'translations': [{'translation': 'Hello'}], 'word_count': 1, 'character_count': 7}) # test when Bonjour is given as input the output is Hello.
        self.assertEqual(frenchtoEnglish("Oui"), {'translations': [{'translation': 'Yes'}], 'word_count': 1, 'character_count': 3})  # test when Oui is given as input the output is Yes.
 
        
class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"), {'translations': [{'translation': 'Bonjour'}], 'word_count': 1, 'character_count': 5}) # test when Hello is given as input the output is Bonjour.
        self.assertEqual(englishToFrench("Yes"), {'translations': [{'translation': 'Oui'}], 'word_count': 1, 'character_count': 3}) # test when Yes is given as input the output is Oui

unittest.main()