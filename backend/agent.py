import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEYS = os.getenv("PERPLEXITY_API_KEY")
BASE_URL = os.getenv("PERPLEXITY_BASE_URL", "https://api.perplexity.ai")
MODEL = os.getenv("PERPLEXITY_MODEL", "sonar-medium-online")

def generate_instagram_post(product_name, features, style_example):
    prompt = (
        f'Write a catchy Instagram caption for a female clothing product whose theme is Ethnic prints, modern mood and major main character vibes!!. \n'
        f'Product: {product_name} \n'
        f'Features: {features} \n'
        f'Style Example: {style_example} \n'
        f'Include relevant hashtags and a call to action.'
    )
    headers = {
        'Authorization': f'Bearer {API_KEYS}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'model': MODEL,
        'messages': [{'role':'user', 'content':prompt}]
    }
    
    response = requests.post(f'{BASE_URL}/v1/chat/completions', headers=headers, json=data)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']
    