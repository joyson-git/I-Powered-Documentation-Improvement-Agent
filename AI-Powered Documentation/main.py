# Import the function that uses Gemini AI to analyze given text and URL
from utils.llm_agent import analyze_with_gemini

# Import the function that fetches and cleans HTML/text content from a given URL
from utils.html_parser import fetch_and_clean_text

# Define the main function to generate a documentation review
def generate_documentation_review(url):
    """
    Fetches and analyzes the content from the given URL.

    Args:
        url (str): The URL of the documentation or webpage to analyze.

    Returns:
        dict: A dictionary containing the analysis result or an error message.
    """
    try:
        # Step 1: Fetch and clean the text content from the given URL
        text = fetch_and_clean_text(url)

        # Step 2: Analyze the cleaned text using Gemini model
        analysis = analyze_with_gemini(text, url)

        # Step 3: Return the analysis results
        return analysis

    except Exception as e:
        # If any error occurs (e.g., network issue, invalid URL, etc.), return the error as a dictionary
        return {"error": str(e)}


#  uvicorn server:app --reload --port 8005
