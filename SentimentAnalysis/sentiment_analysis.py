import requests
import json

def sentiment_analyzer(analysis_text):
    """Define function for the sentiment analyser"""

    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Custom header specifying the model ID for the sentiment analysis service
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # The text to be analysed
    text_to_analyse = analysis_text

     # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json = myobj, headers=headers)

    # Parsing the JSON response from the API
    response_json = json.loads(response.text)

    # Extracting sentiment label and score from the response
    label = response_json["documentSentiment"]["label"]
    score = response_json["documentSentiment"]["score"]
    sentiment_label_score = {"label": label, "score": score}
    
    return sentiment_label_score