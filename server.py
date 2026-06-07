from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Emotion Detector is running!"

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get('textToAnalyze')

    if text is None or text.strip() == "":
        return "Invalid input! Try again."

    result = emotion_detector(text)

    if result is None:
        return "Error in processing"

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)