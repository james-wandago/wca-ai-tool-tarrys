import os
import requests

API_KEY = os.getenv("ANTHROPIC_API_KEY")

def get_ai_response(service, client_request):
    url = "https://api.anthropic.com/v1/messages"
    
    headers = {
        "x-api-key": API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    
    prompt = f"""You are a professional beauty and tattoo expert at Tarrys Beauty Lounge in Nairobi.

Client wants: {service}
Request: {client_request}

Provide:
1. Best service recommendation
2. Price range in Kenyan Shillings (KES)
3. A short professional message to send to the client"""

    data = {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    
    print("Calling Claude API...")
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        print("\n" + result['content'][0]['text'])
    else:
        print("API Error:", response.status_code, response.text)

if __name__ == "__main__":
    if not API_KEY:
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("Run: $env:ANTHROPIC_API_KEY=\"your-key-here\"")
    else:
        service = input("Enter service: ")
        client_request = input("Enter client request: ")
        get_ai_response(service, client_request)