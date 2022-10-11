import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')

def english_to_french(engtext):
    """
    function to translate english to french
    """
    translation = language_translator.translate(
            text=engtext, model_id='en-fr').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return engtext

def french_to_english(frtext):
    """
    function to translate french to english
    """
    translation = language_translator.translate(
            text=frtext, model_id='fr-en').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return frtext

