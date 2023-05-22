#!/usr/bin/python3
import unittest
import json

from translator import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):


    def test_englishToFrench(self):

        result = englishToFrench('Hello')

        self.assertEqual(result, 'Bonjour')
        self.assertNotEqual(result, 'Hello')

    def test_frenchToEnglish(self):

        result = frenchToEnglish('Bonjour')

        self.assertEqual(result, 'Hello')
        self.assertNotEqual(result, 'Bonjour')


    def test_englishToFrench_with_null_input(self):

        result = englishToFrench(None)
        self.assertIsNone(result)


    def test_frenchToEnglish_with_null_input(self):
        
        result = frenchToEnglish(None)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
