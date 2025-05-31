from requests_html import AsyncHTMLSession  # Importing async HTML session for rendering JavaScript pages

# Create a single asynchronous HTML session
asession = AsyncHTMLSession()

# Define an asynchronous function to fetch and clean text from a URL
async def fetch_and_clean_text(url):
    response = await asession.get(url)       # Send asynchronous GET request to the URL
    await response.html.arender()            # Render JavaScript (for dynamic content loading)
    return response.html.text                # Return the visible text content of the web page
