from flask import Flask, request, render_template
from EmotionDetection import emotion_detector


app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detector_route():
   
    text_to_analyze = request.args.get('textToAnalyze')
    

    response = emotion_detector(text_to_analyze)
   

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    formatted_response = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    
    return formatted_response

@app.route("/")
def render_index_page():
    
    return render_template('index.html')

if __name__ == "__main__":
    # Run the Flask application on localhost:5000
    app.run(host="0.0.0.0", port=5000, debug=True)
    #app.run(debug=True)