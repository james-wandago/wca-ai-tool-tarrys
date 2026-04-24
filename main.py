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
    
<<<<<<< HEAD
    prompt = f"""You are a professional beauty and tattoo consultant based in Nairobi, Kenya.
You have 10 years of experience in nails, lashes, makeup, skincare, and tattoos.
You understand the local Kenyan market, current beauty trends, and Kenyan Shilling pricing.

When given a client beauty or tattoo request, you must do THREE things:
1. Identify and recommend the best matching service for the client.
2. Suggest a realistic PRICE RANGE in KES based on current Kenyan salon rates.
3. Write a SHORT, PROFESSIONAL client message the salon owner can send via WhatsApp.

Context:
- Location: Nairobi, Kenya
- Currency: Kenyan Shillings (KES) - do not use USD or GBP
- Services include: Nails: acrylic, gel, shellac, nail art. Lashes: Classic, volume, hybrid

Constraints:
1. Always include price range in Kenyan Shillings (KES)
2. Keep client message under 50 words
3. Be professional and friendly

=======
    prompt = f"""You are a professional beauty and tattoo expert.
    
>>>>>>> c77b19c8794f8a1b6c41f49def6c368c825e8845
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
<<<<<<< HEAD
    # TEMP MOCK FOR SUBMISSION - delete when admin sends funded key
=======
    # TEMP MOCK FOR SUBMISSION - admin adding credits
>>>>>>> c77b19c8794f8a1b6c41f49def6c368c825e8845
    print("""
Service Recommendation: Gel Bridal Nail Set with Custom Nail Art
Price Range: KES 3500 - 5000
Client Message: Hi! For your wedding we recommend our Gel Bridal Set with custom nail art. Price KES 3500-5000. Includes free consultation. Book now to secure your slot!
""")
    return
    
    # Real API call below - uncomment when you get key
    # response = requests.post(url, headers=headers, json=data)
<<<<<<< HEAD
    # return response.json()["content"][0]["text"]
=======
    # print(response.json())
>>>>>>> c77b19c8794f8a1b6c41f49def6c368c825e8845

if __name__ == "__main__":
    service = input("Enter service: ")
    request = input("Enter client request: ")
<<<<<<< HEAD
    get_ai_response(service, request)
=======
    get_ai_response(service, request)
>>>>>>> c77b19c8794f8a1b6c41f49def6c368c825e8845
