import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the Watson Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers required by the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input payload
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Sending a POST request to the API
    response = requests.post(url, json=myobj, headers=headers)
    
    # Parsing the JSON response text
    formatted_response = json.loads(response.text)
    
    # Extracting the target emotions from the response structure
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotion_predictions['anger']
    disgust_score = emotion_predictions['disgust']
    fear_score = emotion_predictions['fear']
    joy_score = emotion_predictions['joy']
    sadness_score = emotion_predictions['sadness']
    
    # Building a local dictionary of emotions to find the highest score
    emotions_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # Determining the dominant emotion based on the maximum score value
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)
    
    # Appending the dominant emotion to our final payload format
    emotions_dict['dominant_emotion'] = dominant_emotion
    
    return emotions_dict
