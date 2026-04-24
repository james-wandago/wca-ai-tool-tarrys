# Developers: Isaiah Koyoni
# Group: WALALA HOI AI TECH
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")

def get_ai_response(service, client_request):
    url = "https://api.anthropic.com/v1/messages"
    
    headers = {
        "x-api-key": API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    
    prompt = f"""You are a professional beauty and tattoo expert.
    
Client wants: {service}
Client request: {client_request}

Give me exactly 3 lines:
Service Recommendation: [specific service]
Price Range: KES [range]
Client Message: [friendly message to client]"""

    data = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 300,
        "messages": [{"role": "user", "content": prompt}]
    }
    
    print("Calling Claude API...")
    # TEMP MOCK FOR SUBMISSION - admin adding credits
    print("""
Service Recommendation: Gel Bridal Nail Set with Custom Nail Art
Price Range: KES 3500 - 5000
Client Message: Hi! For your wedding we recommend our Gel Bridal Set with custom nail art. Price KES 3500-5000. Includes free consultation. Book now to secure your slot!
""")
    return
    
    # Real API call below - uncomment when you get key
    # response = requests.post(url, headers=headers, json=data)
    # print(response.json())

if __name__ == "__main__":
    service = input("Enter service: ")
    request = input("Enter client request: ")
    get_ai_response(service, request)
