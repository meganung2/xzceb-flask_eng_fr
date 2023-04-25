import unittest

from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), 'Hello') # test when Bonjour is given as input the output is Hello.
        self.assertEqual(french_to_english("Oui"), "Yes")  # test when Oui is given as input the output is Yes.
 
        
class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test when Hello is given as input the output is Bonjour.
        self.assertEqual(english_to_french("Yes"), "Oui") # test when Yes is given as input the output is Oui

unittest.main()