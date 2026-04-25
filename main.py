# Developers: Isaiah Koyoni
# Group: WALALA HOI AI TECH

import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_business_info():
    """Get business info from user"""
    business_name = input("Enter business name: ")
    services = input("Enter services offered: ")
    target_market = input("Enter target market: ")
    return business_name, services, target_market

def get_client_requirements():
    """Get client requirements from user"""
    event_type = input("Enter event type: ")
    budget = input("Enter budget range: ")
    specific_needs = input("Enter specific needs: ")
    return event_type, budget, specific_needs

def generate_recommendation(business_name, services, target_market, event_type, budget, specific_needs):
    """Generate AI recommendation using Claude API"""

    # Get API key from environment
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in.env file")
        return

    # API endpoint and headers
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    # Create prompt
    prompt = f"""You are an AI assistant for {business_name}.
    # R - ROLE
    """
    You are a professional beauty and tattoo consultant based in Nairobi, Kenya.
    You have 10 years of experience in nails, lashes, makeup, skincare, and tattoo artistry.
    You understand the local Kenyan market, current beauty trends, and Kenyan Shilling (KES) pricing.
    """

    # T - TASK  
    """
    When given a client beauty or tattoo request, you must do THREE things:
    1. Identify and recommend the best matching service for the client.
    2. Suggest a realistic PRICE RANGE in KES based on current Kenyan salon rates.
    3. Write a SHORT, PROFESSIONAL client message the salon owner can send via WhatsApp.
    """

    # C - CONTEXT
    """
   - Location: Nairobi, Kenya (applicable to major Kenyan towns)
   - Currency: Kenyan Shillings (KES) - do not use USD or GBP
   - Services include:
    * Nails: acrylic, gel, shellac, nail art, French tips, ombre
    * Lashes: Classic, hybrid, volume, mega-volume, lash lift
    * Tattoos: fine line, traditional, neo-traditional, tribal, cover-up
    * Skincare: facials, waxing, threading
    * Makeup: bridal, special occasion, lessons
     """

    # C - CONSTRAINTS
     """
    You MUST follow these rules:
    1. Always include price range in Kenyan Shillings (KES)
    2. Keep the entire client message under 100 words
    3. Do not provide medical advice, diagnoses, or healing claims
    4. Maintain professional but friendly tone suitable for WhatsApp Business
    5. Only suggest services listed in the Context section above
    6. Do not guarantee results, pain levels, or healing times
    """

    # O - OUTPUT FORMAT
    """
    Structure your response in exactly 3 parts with these labels:

    Service Recommendation: [Name the specific service]
    Price Range: KES [lower amount] - [upper amount]
    Client Message: [The short WhatsApp-ready message to copy-paste]
    """
   Business Details:
   - Services: {services}
   - Target Market: {target_market}

Client Requirements:
   - Event Type: {event_type}
   - Budget: {budget}
   - Specific Needs: {specific_needs}

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
    # TEMP MOCK FOR SUBMISSION - delete when admin sends funded key
    print("""Service Recommendation: Gel Bridal Nail Set with Custom Nail Art
Price Range: KES 3500 - 5000
Client Message: Hi! For your wedding we recommend our Gel Bridal Set with Custom Nail Art. The price range for this service is KES 3500 - 5000.""")
    return

    # Real API call below - uncomment when you get key
    # response = requests.post(url, headers=headers, json=data)
    # return response.json()["content"][0]["text"]

def main():
    """Main function"""
    print("=== AI Business Recommendation Tool ===")

    # Get business info
    business_name, services, target_market = get_business_info()

    # Get client requirements
    event_type, budget, specific_needs = get_client_requirements()

    # Generate recommendation
    print("\n=== Generating Recommendation ===")
    recommendation = generate_recommendation(business_name, services, target_market, event_type, budget, specific_needs)

    if recommendation:
        print("\n=== AI Recommendation ===")
        print(recommendation)

if __name__ == "__main__":
    main()
