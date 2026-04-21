# ============================================================
# BEAUTY & TATTOO AI ASSISTANT
# Developer: [Your Name]
# Group: [Your Group Name]
# We Can Academy - AI Course End of Module Project
# ============================================================

import anthropic
import json
import os


# ============================================================
# SECTION 1: API SETUP
# Configure the Anthropic (Claude) API with your key
# ============================================================

# SECTION 1: API SETUP
# Get API key from environment variable, or prompt user if not set
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
if not API_KEY:
    API_KEY = input("Enter your Anthropic API key: ").strip()
    
# Create the Anthropic client
client = anthropic.Anthropic(api_key=API_KEY)

# Claude model to use (Sonnet 4 is the latest as of 2026)
MODEL_NAME = "claude-haiku-4-5-20251001"


# ============================================================
# SECTION 2: R-T-C-C-O PROMPT DESIGN
# Role - Task - Context - Constraints - Output
# This prompt tells the AI exactly how to behave
# ============================================================

def build_prompt(client_request):
    """
    Builds the R-T-C-C-O prompt to send to the AI.
    Returns a formatted string.
    """
    
    prompt = f"""You are a professional Beauty & Tattoo Salon Consultant based in Nairobi, Kenya.

ROLE:
You are an expert beauty advisor with 10 years of experience in nail art, eyelash extensions, permanent makeup, and tattoo design. You understand Kenyan beauty trends, local pricing, and professional client communication.

TASK:
Analyze the client's request below and provide:
1. The best service recommendation
2. A realistic price range in Kenyan Shillings (KES)
3. A professional, warm message the salon owner can send to the client via WhatsApp or SMS

CONTEXT:
- You are advising a small-to-medium beauty salon or tattoo studio in Kenya
- Prices should reflect the Kenyan market (not US or UK prices)
- Clients typically communicate via WhatsApp
- The salon wants to sound professional but friendly

CONSTRAINTS:
- Price range must be in KES only
- Keep the response strictly in JSON format
- Do not include markdown formatting (no ```json blocks)
- If the request is unclear, still provide your best recommendation
- Keep the WhatsApp message under 150 words
- Be respectful and professional at all times

OUTPUT FORMAT:
Return ONLY a valid JSON object with this exact structure:
{{
    "service_recommendation": "Name of the recommended service",
    "price_range_kes": "X,XXX - X,XXX KES",
    "duration_estimate": "Approximate time",
    "professional_message": "The exact WhatsApp message to send",
    "notes": "Any extra advice for the salon owner"
}}

CLIENT REQUEST:
{client_request}
"""
    return prompt


# ============================================================
# SECTION 3: GET USER INPUT
# Accept client request from the salon owner
# ============================================================

def get_user_input():
    """
    Displays welcome banner and gets the client's request.
    Returns the request as a string.
    """
    print("\n" + "=" * 60)
    print("💅 BEAUTY & TATTOO AI ASSISTANT 💅")
    print("Powered by Claude AI (Anthropic)")
    print("=" * 60 + "\n")
    
    # Get input from the salon owner
    request = input("📝 Enter client request: ")
    
    # If user presses Enter without typing, use a demo example
    if not request.strip():
        request = "gel nails with glitter for a wedding"
        print(f"(Using demo example: {request})")
    
    return request


# ============================================================
# SECTION 4: API INTEGRATION
# Send the prompt to Claude and get the AI response
# ============================================================

def get_ai_recommendation(client_request):
    """
    Sends the client request to the Claude API.
    Returns the parsed JSON response as a Python dictionary.
    """
    
    # Build the full R-T-C-C-O prompt
    full_prompt = build_prompt(client_request)
    
    try:
        # Send request to Claude API
        response = client.messages.create(
            model=MODEL_NAME,
            max_tokens=1000,  # Maximum response length
            messages=[
                {
                    "role": "user",
                    "content": full_prompt
                }
            ]
        )
        
        # Extract the text from Claude's response
        raw_text = response.content[0].text
        
        # Clean up the response (remove markdown code blocks if present)
        clean_text = raw_text.replace("```json", "").replace("```", "").strip()
        
        # Parse the JSON string into a Python dictionary
        recommendation = json.loads(clean_text)
        
        return recommendation
        
    except json.JSONDecodeError:
        # If Claude didn't return valid JSON, return the raw text instead
        return {
            "service_recommendation": "Could not parse AI response",
            "price_range_kes": "N/A",
            "duration_estimate": "N/A",
            "professional_message": raw_text,
            "notes": "The AI returned non-JSON output. Showing raw response."
        }
        
    except Exception as e:
        # Handle any API errors (no internet, invalid key, etc.)
        return {
            "service_recommendation": "Error",
            "price_range_kes": "N/A",
            "duration_estimate": "N/A",
            "professional_message": f"API Error: {str(e)}",
            "notes": "Please check your API key and internet connection."
        }


# ============================================================
# SECTION 5: DISPLAY RESULTS
# Format and print the AI recommendation nicely
# ============================================================

def display_recommendation(data):
    """
    Takes the parsed JSON dictionary and prints it in a readable format.
    """
    print("\n" + "=" * 60)
    print("✅ AI RECOMMENDATION")
    print("=" * 60)
    
    print(f"\n💡 Service: {data.get('service_recommendation', 'N/A')}")
    print(f"💰 Price Range: {data.get('price_range_kes', 'N/A')}")
    print(f"⏱️  Duration: {data.get('duration_estimate', 'N/A')}")
    
    print(f"\n📱 WhatsApp Message to Client:")
    print("-" * 40)
    print(data.get('professional_message', 'N/A'))
    print("-" * 40)
    
    if data.get('notes'):
        print(f"\n📝 Notes: {data.get('notes')}")
    
    print("=" * 60)


# ============================================================
# SECTION 6: MAIN PROGRAM LOOP
# Runs the tool and asks if user wants to process another request
# ============================================================

def main():
    """
    Main function that runs the Beauty & Tattoo AI Assistant.
    Loops until the user chooses to exit.
    """
    
    while True:
        # Step 1: Get input from salon owner
        client_request = get_user_input()
        
        # Step 2: Get AI recommendation from Claude
        print("\n⏳ Thinking... contacting Claude AI...")
        recommendation = get_ai_recommendation(client_request)
        
        # Step 3: Display the results
        display_recommendation(recommendation)
        
        # Step 4: Ask if they want to process another client
        again = input("\n🔄 Process another client request? (yes/no): ").strip().lower()
        
        if again != 'yes':
            print("\n👋 Thank you for using Beauty & Tattoo AI Assistant!")
            print("Goodbye!\n")
            break


# ============================================================
# SECTION 7: PROGRAM ENTRY POINT
# This ensures main() only runs when we execute this file directly
# ============================================================

if __name__ == "__main__":
    main()