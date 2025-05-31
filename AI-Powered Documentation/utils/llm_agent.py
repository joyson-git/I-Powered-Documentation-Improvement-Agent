import requests
import json

# Gemini API key and endpoint
GEMINI_API_KEY = "AIzaSyAWpL9rM_Ca0fWhDBSzKryQtV0jMYFx7F4"
GEMINI_ENDPOINT = (
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
)

def analyze_with_gemini(article_text: str, url: str) -> dict:
    prompt = f"""
You are an expert technical writer tasked with improving documentation. Analyze the article below and provide a structured report.

ARTICLE URL: {url}

ARTICLE CONTENT:
{article_text}

Evaluate it based on these criteria:

1. Readability for a Marketer:
- Explain how readable it is for a non-technical marketer.
- Mention if sentences are too complex, jargon is used, or tone is off.

2. Structure and Flow:
- Is the information well-structured and logically flowing?
- Are headings used effectively?

3. Completeness of Information and Examples:
- Does it explain the concept/feature well?
- Are examples missing, unclear, or insufficient?

4. Adherence to Style Guidelines (use Microsoft Style Guide as base):
- Voice and Tone: Is it clear, friendly, and direct?
- Clarity and Conciseness: Are there unnecessary words or complexity?
- Action-oriented Language: Does it guide the user?

Return a structured, detailed list of suggestions with reasoning and suggested edits.
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(
            f"{GEMINI_ENDPOINT}?key={GEMINI_API_KEY}",
            headers={"Content-Type": "application/json"},
            json=payload
        )

        response.raise_for_status()
        result = response.json()

        if "candidates" in result and result["candidates"]:
            return {
                "url": url,
                "analysis": result["candidates"][0]["content"]["parts"][0]["text"]
            }
        else:
            return {"error": "No content returned from Gemini"}

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
