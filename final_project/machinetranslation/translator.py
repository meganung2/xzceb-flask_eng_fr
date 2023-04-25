'''py
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['auWnFivrjl4AQV6p7B8WuvEWh7wMF5KLBccOTONzFosd']
url = os.environ['https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/d4fcdf96-13e1-4ec5-a09e-13100ccb4810']
'''

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('auWnFivrjl4AQV6p7B8WuvEWh7wMF5KLBccOTONzFosd')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/d4fcdf96-13e1-4ec5-a09e-13100ccb4810')

translation = language_translator.translate(
    text='Hello, how are you today?',
    model_id='en-fr').get_result()

def english_to_french(english_text):
    ''' to translate english to french'''
    french_text = language_translator.translate(
    english_text,
    model_id='en-fr').get_result()
    return french_text

def french_to_english(french_text):
    ''' to translate french to english'''
    english_text = language_translator.translate(
    french_text,
    model_id='fr-en').get_result()
    return english_text
