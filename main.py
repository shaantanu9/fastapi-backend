
# Import FastAPI reason to use this import is to create a FastAPI instance
from fastapi import FastAPI 
# Import middleware CorsMiddleware is to handle CORS (Cross-Origin Resource Sharing) and allow requests from different origins
from fastapi.middleware.cors import CORSMiddleware # Import CORSMiddleware
# Import StaticFiles is to serve static files (like HTML, CSS, JS) from a directory
from fastapi.staticfiles import StaticFiles

app = FastAPI() # Create a FastAPI instance this instance will be used to define the API routes and handle requests and responses and middleware
# Add CORS middleware to allow requests from different origins
app.add_middleware(
    CORSMiddleware,
    # Specify the origins that are allowed to make requests to the API
    # In this case, we are allowing all origins by using "*"
    # In a production environment, you should specify the allowed origins explicitly
    # For example: allow_origins=["https://example.com"]
    # This is important for security reasons to prevent unauthorized access to your API
    # In this case, we are allowing all origins by using "*"
    allow_origins=["*"],  # Allow all origins
    # Specify the headers that are allowed in the requests
    # In this case, we are allowing all headers by using "*"
    # This is important for security reasons to prevent unauthorized access to your API
    # In a production environment, you should specify the allowed headers explicitly
    allow_credentials=True,
    # Allow credentials (like cookies) to be included in the requests
    # This is important for security reasons to prevent unauthorized access to your API
    # use of allow credentials=True is important for security reasons to prevent unauthorized access to your API
    allow_methods=["*"],  # Allow all HTTP methods
    # Specify the HTTP methods that are allowed in the requests
    # In this case, we are allowing all HTTP methods by using "*"
    # This is important for security reasons to prevent unauthorized access to your API
    allow_headers=["*"],  # Allow all headers
)


# Simple Health Check Endpoint
@app.get("/")
async def root()-> dict[str:str]: # Define a root endpoint that returns a simple message:
    return {"message": "Hello World!"}
# Serve static files from the "frontend" directory

@app.get("/api")
async def api() -> str:
    return "Hello from the API!"