# Importing FastAPI to create the web application and Request to handle incoming HTTP request bodies
from fastapi import FastAPI, Request

# Importing CORS middleware to allow cross-origin requests (i.e., requests from different domains like frontend on localhost)
from fastapi.middleware.cors import CORSMiddleware

# Importing the main function that performs documentation review (not used directly in this code, possibly used elsewhere)
from main import generate_documentation_review

# Importing a utility function to fetch and clean text from a given URL
from utils.html_parser import fetch_and_clean_text

# Importing the function that performs analysis using Google's Gemini model
from utils.llm_agent import analyze_with_gemini

# Creating an instance of the FastAPI application
app = FastAPI()

# Adding CORS middleware to the FastAPI app
# This allows requests from the specified origin (like frontend running on Vite dev server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Only allow frontend running on this URL to make requests
    allow_credentials=True,                   # Allow sending cookies, auth headers, etc.
    allow_methods=["*"],                      # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],                      # Allow all headers in the requests
)

# Define an endpoint `/analyze/` that listens for POST requests
@app.post("/analyze/")
async def analyze(request: Request):
    # Parse the incoming request JSON body
    data = await request.json()
    
    # Extract the `url` field from the request JSON
    url = data.get("url")
    
    try:
        # Use the utility function to fetch and clean text content from the given URL
        text = await fetch_and_clean_text(url)  # Await is necessary because the function is asynchronous
        
        # Analyze the cleaned text using Gemini AI model and include the URL for context
        analysis = analyze_with_gemini(text, url)
        
        # Return the result as a JSON response
        return {"analysis": analysis}
    
    except Exception as e:
        # If there's an error during fetch/analysis, return the error message
        return {"error": str(e)}
