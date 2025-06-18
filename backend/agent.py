import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("PERPLEXITY_API_KEY")
BASE_URL = os.getenv("PERPLEXITY_BASE_URL", "https://api.perplexity.ai")
MODEL = os.getenv("PERPLEXITY_MODEL", "sonar-pro")

def generate_instagram_post(product_name, features, style_example):
    prompt = (
        f"Write a catchy Instagram caption for a female clothing product whose theme is Ethnic prints, modern mood and major main character vibes!!\n"
        f"Product: {product_name}\n"
        f"Features: {features}\n"
        f"Style Example: {style_example}\n"
        f"Include relevant hashtags and a call to action."
    )
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    print(headers)
    print(data)
    try:
        response = requests.post(f"{BASE_URL}/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        print(f"Perplexity API error: {e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"Response body: {e.response.text}")
        return "Error generating caption. Please try again."
