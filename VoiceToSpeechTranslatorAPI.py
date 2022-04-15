import json
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
import urllib.request

#                   speech to text authenticator
url_s2t = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/0851cc8b-75a1-4463-b814-3e2ae43f69a7"
iam_apikey_s2t = "5ofKNDxKXeuZ6PUH3c0le6HnDChCf8qIR1mFY1WWB06s"
s2t_authenticator = IAMAuthenticator(iam_apikey_s2t)
speech_to_text = SpeechToTextV1(
    authenticator=s2t_authenticator
)
speech_to_text.set_service_url(url_s2t)

#            file retrival   +  speech to text conversion
filename = urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/PolynomialRegressionandPipelines.mp3")
with open(filename[0],mode="rb") as wav:
     res = speech_to_text.recognize(audio=wav,content_type='audio/mp3').get_result()
     res_filltered = res['results'][0]['alternatives'][0]['transcript']

    #                translator Authenticator
api_key_lt = 'jrZslO2zBTYpjbz9DeVjejNcV1OCdsJp2XwGkb4Tm8Qt'
api_url_lt = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/060f7456-7ee1-4d82-bace-b852715d49ee'
model_id = 'en-es'
lt_authenticator = IAMAuthenticator(api_key_lt)
language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=lt_authenticator
        )

language_translator.set_service_url(api_url_lt )
    #                   translator
text_to_translate = res_filltered
translation = language_translator.translate(text = text_to_translate,model_id = model_id).get_result()
translationFil = translation['translations'][0]['translation']
print(json.dumps(translationFil, indent=2, ensure_ascii=False))

#                  writing the transcript to text file "transcript.txt"
with open('transcript.txt','w',encoding="utf-8") as x :
    x.write(translationFil)
