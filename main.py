import requests

API_KEY = "your_gemini_api_key_here"

def get_ai_response(service, client_request):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

    prompt = f"""
You are a professional beauty and tattoo expert at Tarrys Beauty Lounge in Kenya.

Client wants: {service}
Request: {client_request}

Provide:
1. Best service recommendation
2. Price range in Kenyan Shillings (KES)
3. A short professional message to send to the client
"""

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"Error: {response.text}"


# ---- USER INPUT ----
service = input("Enter service (nails, lashes, tattoo, etc): ")
client_request = input("Enter client request: ")

# ---- AI CALL ----
output = get_ai_response(service, client_request)

# ---- DISPLAY ----
print("\n--- AI RESPONSE ---")
print(output)
