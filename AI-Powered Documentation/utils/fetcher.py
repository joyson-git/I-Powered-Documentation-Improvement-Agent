import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing and navigating HTML

# Function to fetch and extract main article text from a given URL
def fetch_article_text(url):
    response = requests.get(url)  # Send a GET request to the URL
    soup = BeautifulSoup(response.text, 'html.parser')  # Parse the HTML response using BeautifulSoup

    # Try to find the main article content:
    # First look for a <div> with class "article-body", otherwise fallback to the <article> tag
    article = soup.find('div', {'class': 'article-body'}) or soup.find('article')

    # Return the clean text from the found tag (with line breaks between elements), else return empty string
    return article.get_text(separator='\n', strip=True) if article else ""
