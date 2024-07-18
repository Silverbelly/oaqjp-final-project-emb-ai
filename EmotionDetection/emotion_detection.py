''' This module contains methods to call embedded AI analysis tools
    to evaluate the emotional state of feedback responses
'''

import json
import requests
def emotion_detector(text_to_analyze):

    ''' This method calls the emotion predictor at the specified url
    '''

    url = 'https://sn-watson-emotion.labs.skills.network'\
          '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=data, timeout=30)

    if response.status_code == 400:
        return {
                "anger": None, 
                "disgust": None, 
                "fear": None, 
                "joy": None, 
                "sadness": None, 
                "dominant_emotion": None
                }

    # convert to json and extract emotions and scores
    json_response = json.loads(response.text)
    emotion_list = json_response['emotionPredictions'][0]['emotion']

    # evaluate dominant emotion
    dominant_emotion = ""
    current_score = -1.0
    for emotion, score in emotion_list.items():
        if score > current_score:
            current_score = score
            dominant_emotion = emotion
    emotion_list["dominant_emotion"] = dominant_emotion

    return  emotion_list
