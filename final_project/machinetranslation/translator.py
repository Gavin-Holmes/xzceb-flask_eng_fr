'''
Creating a translation api.
'''
#!/usr/bin/python3
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

'''
Declare global variables
'''

apikey = os.environ['apikey']
url = os.environ['url']
ibm_watson_version = '2018-05-01'

def translator_instance(ibm_watson_url, ibm_watson_apikey, ibm_watson_version):
    """
    Create an instance of the IBM Watson Language Translator service.

    Args:
        ibm_watson_url (str): The URL for the IBM Watson Language Translator service.
        ibm_watson_apikey (str): The API key for the IBM Watson Language Translator service.
        ibm_watson_version (str): The version of the IBM Watson Language Translator service.

    Returns:
        LanguageTranslatorV3: An instance of the IBM Watson Language Translator service.
    """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version=ibm_watson_version,
        authenticator=authenticator
    )

    language_translator.set_service_url(url)

    return language_translator

def englishToFrench(english_text):
    """
    Translate English text to French using the IBM Watson Language Translator service.

    Args:
        english_text (str): The English text to be translated.

    Returns:
        str: The translated French text.
    """
    if english_text is None or english_text == '':
        return None

    translation = translator_instance(url, apikey, ibm_watson_version)
    get_french_text = translation.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()

    french_text = json.dumps(get_french_text, indent=2, ensure_ascii=False)
    return json.loads(french_text)['translations'][0]['translation']

#print(englishToFrench('test and some other nonsense'))

def frenchToEnglish(french_text):
    """
    Translate French text to English using the IBM Watson Language Translator service.

    Args:
        french_text (str): The French text to be translated.

    Returns:
        str: The translated English text.
    """
    if french_text is None or french_text == '':
        return None

    translation = translator_instance(url, apikey, ibm_watson_version)
    get_english_text = translation.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()

    english_text = json.dumps(get_english_text, indent=2, ensure_ascii=False)
    return json.loads(english_text)['translations'][0]['translation']

#print(frenchToEnglish('Test et autres non-sens'))
