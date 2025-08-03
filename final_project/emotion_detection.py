import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=input_json, headers=headers)

    if response.status_code = 400:
        return {
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None
                }

    response_data = response.json()

    emotions_data = response_data['emotionPredictions'][0]['emotion']

    anger_score = emotions_data.get('anger', 0)
    disgust_score = emotions_data.get('disgust', 0)
    fear_score = emotions_data.get('fear', 0)
    joy_score = emotions_data.get('joy', 0)
    sadness_score = emotions_data.get('sadness', 0)

    dominant_emotion_data = max(emotions_data, key=emotions_data.get)

    emotions_output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion_data
    }

    return emotions_output