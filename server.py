''' Executing this function initiates the application of emotion
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion():
    ''' Receives the text to be analyzed and returns the dominant emotion
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detector(text_to_analyze)

    if dominant_emotion is None:
        return "Invalid text! Please try again."
    return f"The given text has been identified as {dominant_emotion}."

@app.route("/")
def render_index_page():
    ''' Renders the main application Flask page
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
