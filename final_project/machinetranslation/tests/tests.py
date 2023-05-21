#!/usr/bin/python3
import unittest
from unittest.mock import patch
import json

from translator import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):

    @patch('translator.translator_instance')
    def test_englishToFrench(self, mock_translator_instance):
        mock_translate = mock_translator_instance.return_value
        mock_translate.translate.return_value = {
            'translations': [{'translation': 'Bonjour'}]
        }

        result = englishToFrench('Hello')

        self.assertEqual(result, json.dumps({'translations': [{'translation': 'Bonjour'}]}, indent=2, ensure_ascii=False))

    @patch('translator.translator_instance')
    def test_frenchToEnglish(self, mock_translator_instance):
        mock_translate = mock_translator_instance.return_value
        mock_translate.translate.return_value = {
            'translations': [{'translation': 'Hello'}]
        }

        result = frenchToEnglish('Bonjour')

        self.assertEqual(result, json.dumps({'translations': [{'translation': 'Hello'}]}, indent=2, ensure_ascii=False))

    @patch('translator.translator_instance')
    def test_englishToFrench_with_null_input(self, mock_translator_instance):
        # Ensure translator_instance is not called when input is null
        mock_translate = mock_translator_instance.return_value
        mock_translate.translate.return_value = {
            'translations': [{'translation': 'Bonjour'}]
        }

        result = englishToFrench(None)

        # Assert that translator_instance was not called
        mock_translator_instance.assert_not_called()

        self.assertIsNone(result)

    @patch('translator.translator_instance')
    def test_frenchToEnglish_with_null_input(self, mock_translator_instance):
        # Ensure translator_instance is not called when input is null
        mock_translate = mock_translator_instance.return_value
        mock_translate.translate.return_value = {
            'translations': [{'translation': 'Hello'}]
        }

        result = frenchToEnglish(None)

        # Assert that translator_instance was not called
        mock_translator_instance.assert_not_called()

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
