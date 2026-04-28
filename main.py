import anthropic, json, os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY") or input("Key: ").strip()
client = anthropic.Anthropic(api_key=API_KEY)
MODEL = "claude-haiku-4-5-20251001" # Fixed: Current model name

def build_prompt(req):
    return f"""Return ONLY valid JSON for a Nairobi beauty salon. No text before or after JSON.
{{"service_recommendation":"","price_range_kes":"X,XXX - X,XXX KES","duration_estimate":"","professional_message":"","notes":""}}
CLIENT REQUEST: {req}"""

def get_rec(req):
    try:
        resp = client.messages.create(model=MODEL,max_tokens=500,
            messages=[{"role":"user","content":build_prompt(req)},
                      {"role":"assistant","content":"{"}])
        text = "{" + resp.content[0].text.strip()
        text = text.replace("```json","").replace("```","").strip()
        if not text.startswith("{"): text = "{" + text
        if text.count("}") > 0: text = text[:text.rfind("}")+1]
        return json.loads(text)
    except Exception as e:
        return {"service_recommendation":"Error","price_range_kes":"N/A",
                "duration_estimate":"N/A","professional_message":f"Parse failed: {str(e)}","notes":""}

def show(d):
    print("\n=== AI RECOMMENDATION ===")
    print(f"Service: {d.get('service_recommendation','N/A')}")
    print(f"Price: {d.get('price_range_kes','N/A')}")
    print(f"Duration: {d.get('duration_estimate','N/A')}")
    print(f"\nWhatsApp Message:\n{d.get('professional_message','N/A')}")
    if d.get('notes'): print(f"Notes: {d.get('notes')}")
    print("="*40)

def main():
    while True:
        req = input("\nClient request: ") or "gel nails for wedding"
        print("Thinking...")
        show(get_rec(req))
        if input("Another? yes/no: ").lower()!= 'yes': break
    print("Goodbye!")

if __name__=="__main__": main()