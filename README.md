# Repository for final project
# AI-Based Emotion Detection Application

## Description
This application uses Python, Flask, and the Watson NLP library to analyze text and detect embedded emotions. It takes a user-provided string via a web interface and returns a formatted breakdown of emotions including anger, disgust, fear, joy, and sadness, along with the dominant emotion.

## Project Structure
* `EmotionDetection/`: Core application package containing the analysis logic.
  * `__init__.py`: Package initialization and function exposure.
  * `emotion_detection.py`: Interacts with the Watson NLP API.
* `server.py`: Flask web application server and routing.
* `test_emotion_detection.py`: Unit testing suite.

## Features
* **Watson NLP Integration:** Leverages advanced AI models to predict emotional states from text.
* **Flask Web Server:** Provides a clean web UI and API endpoints.
* **Robust Error Handling:** Seamlessly manages invalid entries and blank text requests.
* **Static Analysis Compliant:** Refactored code meeting strict 10/10 `pylint` code quality metrics.

## How to Run
1. Run the Flask server:
   ```bash
   python3 server.py
