"""
Flask application for Emotion Detection.

This module provides an API endpoint to analyze emotions from input text
and a route to render the index page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("EmotionDetection")


def run_emotion_detection():
    """
    Run the Flask application.

    This function starts the Flask web server, making the application
    accessible on host 0.0.0.0 and port 5000 with debugging enabled.
    """
    app.run(host="0.0.0.0", port=5000, debug=True)


@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint to detect emotions from the provided text.

    This route processes a GET request with the query parameter `textToAnalyze`.
    It uses the `emotion_detector` function to analyze emotions and returns
    the detected emotions along with the dominant emotion.

    Returns:
        str: A formatted string with the detected emotions and their values.
        int: HTTP status code (400) if the input text is missing.
    """
    text_to_detect = request.args.get('textToAnalyze')

    if not text_to_detect:
        return "No text provided! Please try again with valid input.", 400

    response = emotion_detector(text_to_detect)
    if response.get('dominant_emotion') is None:
        return "Invalid response! Please try again."

    return (
        f"For the given statement, the system response is: 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']}, and 'sadness': {response['sadness']}. "
        f"The dominant emotion is '{response['dominant_emotion']}'."
    )


@app.route("/")
def render_index_page():
    """
    Render the index page for the application.

    This route renders the `index.html` template, which serves as the
    homepage of the application.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    run_emotion_detection()
