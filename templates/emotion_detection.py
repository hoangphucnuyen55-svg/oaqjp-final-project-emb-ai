import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the Watson Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers required by the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input payload formatted as expected by the Watson service
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Sending a POST request to the API
    response = requests.post(url, json=myobj, headers=headers)
    
    # Returning the raw text response text for the initial validation step
    return response.text
