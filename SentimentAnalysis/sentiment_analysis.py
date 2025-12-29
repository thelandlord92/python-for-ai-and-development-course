import requests
import json

def sentiment_analyzer(analysis_text):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    text_to_analyse = analysis_text
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    response_json = json.loads(response.text)
    label = response_json["documentSentiment"]["label"]
    score = response_json["documentSentiment"]["score"]
    sentiment_label_score = {"label": label, "score": score}
    return sentiment_label_score