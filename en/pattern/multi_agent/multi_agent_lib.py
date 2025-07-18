import boto3

def get_bedrock_response(prompt, model_id):
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')

    response = bedrock.converse(
        modelId=model_id,
        messages=[{"role": "user", "content": [{"text": prompt}]}],
        inferenceConfig={"maxTokens": 2000, "temperature": 0.0}
    )

    return response['output']['message']['content'][0]['text']

def summarize_news(news):
    prompt = f"Please summarize the following news in one sentence:\n\n{news}"
    return get_bedrock_response(prompt, "anthropic.claude-3-5-haiku-20241022-v1:0")

def analyze_sentiment(summary):
    prompt = f"Please analyze the sentiment of the following news summary and evaluate as either 'Positive', 'Neutral', or 'Negative':\n\n{summary}"
    return get_bedrock_response(prompt, "anthropic.claude-3-5-haiku-20241022-v1:0")

def classify_topic(summary):
    prompt = f"Please classify the topic of the following news summary as either 'Politics', 'Economy', 'Society', 'Technology', or 'Culture':\n\n{summary}"
    return get_bedrock_response(prompt, "anthropic.claude-3-5-haiku-20241022-v1:0")

