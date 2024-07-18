''' This initiates the emotion detection application
    over the Flask channel
'''

# imports
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# initialize the app
app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def emo_detector():
    ''' This method receives the text to analyze
        and returns the list of evaulated emotions
        along with the dominant emotion
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    formatted_response = "For the given statement, the system response is "
    counter = 0
    for emotion, score in response.items():
        counter += 1
        if counter == len(response)-1:
            formatted_response = formatted_response[0:len(formatted_response)-2] \
                               + f" and '{emotion}': {score}."
        elif counter == len(response):
            formatted_response += f" The dominant emotion is {response['dominant_emotion']}."
        else:
            formatted_response += f"'{emotion}': {score}, " 
    return formatted_response

@app.route('/')
def render_index_page():
    ''' This method shows the home page for the application
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

