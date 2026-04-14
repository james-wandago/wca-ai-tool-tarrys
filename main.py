import requests

API_KEY = "your_api_key_here"

def get_ai_response(service, client_request):
    url = "https://api.openai.com/v1/chat/completions"

    prompt = f"""
You are a beauty and tattoo expert at Tarrys Beauty Lounge in Kenya.

A client wants: {service}
Request: {client_request}

Provide:
1. Best service recommendation
2. Price range in KES
3. A professional message to send to the client
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4.1-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        return response.text


service = input("Enter service: ")
client_request = input("Enter client request: ")

output = get_ai_response(service, client_request)

print("\n--- AI RESPONSE ---")
print(output)
