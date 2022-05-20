'''
module for translating from english to french and french to englisch
'''
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION='2018-05-01'

AUTHENTICATOR = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=AUTHENTICATOR
)

language_translator.set_service_url(URL)

def english_to_french(english_text):
    '''
    method takes englishText as string and return its translation to frenchText as string
    '''
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text=translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    '''
    method takes frenchText as string and return its translation to englishText as string
    '''
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text=translation['translations'][0]['translation']
    return english_text
