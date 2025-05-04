
# Import FastAPI reason to use this import is to create a FastAPI instance
from fastapi import FastAPI, HTTPException # Import FastAPI and HTTPException
# Import middleware CorsMiddleware is to handle CORS (Cross-Origin Resource Sharing) and allow requests from different origins
from fastapi.middleware.cors import CORSMiddleware # Import CORSMiddleware
# Import StaticFiles is to serve static files (like HTML, CSS, JS) from a directory
from fastapi.staticfiles import StaticFiles
from enum import Enum # Import Enum is to define an enumeration for the genres of the bands

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

# 

band = [
    {"id": 121, "name": "Band 1", "genre": "ROCK"},
    {"id": 2, "name": "Band 2", "genre": "Pop"},
    {"id": 3, "name": "Band 3", "genre": "Jazz"},
    {"id": 4, "name": "Band 4", "genre": "Classical"},
    {"id": 5, "name": "Band 5", "genre": "Hip Hop"},
    {"id": 6, "name": "Band 6", "genre": "Country"},
    {"id": 7, "name": "Band 7", "genre": "Reggae"},
    {"id": 8, "name": "Band 8", "genre": "Blues"},
    {"id": 9, "name": "Band 9", "genre": "Metal"},
    {"id": 10, "name": "Band 10", "genre": "Folk"},
    {"id": 11, "name": "Band 11", "genre": "Electronic"},
    {"id": 12, "name": "Band 12", "genre": "Indie"},
    {"id": 13, "name": "Band 13", "genre": "Punk"},
    {"id": 14, "name": "Band 14", "genre": "Alternative"},
    {"id": 15, "name": "Band 15", "genre": "R&B"},
]

# Simple Health Check Endpoint
@app.get("/api", tags=["Health Check"], summary="Health Check", status_code=200, description="This is a simple health check endpoint to check if the API is running")
async def api() -> str:
    return "Hello from the API!, this is a simple health check endpoint to check if the API is running"

# Endpoint to get all bands
@app.get("/api/bands")
async def get_bands() -> list[dict]:
    """
    Endpoint to get all bands 22
    """
    return band

# Endpoint to get a band by ID
@app.get("/api/bands/{band_id}")
async def get_band(band_id: int) -> dict:
    """
    Endpoint to get a band by ID
    """
    for b in band:
        if b["id"] == band_id:
            return b
    return {"error": "Band not found"}

# Endpoint to create a new band
@app.post("/api/bands/create")
async def create_band(band_data:dict) -> dict:
    """
    Endpoint to crate a new band in the database
    """

    breakpoint = band_data["name"].index(" ")
    print(breakpoint)
    # Before creating need to check if the bank already exists
    for b in band:
        if b["name"] == band_data["name"]: # use of breakpoint is 
            raise HTTPException(status_code=404, detail="Band already exists")
    # If the band does not exist, create a new band
    new_band = {
        "id": len(band) + 1,
        "name": band_data["name"],
        "genre": band_data["genre"]
    }
    band.append(new_band)
    return new_band

# @app.get("/api/bands/genre/{genre}", response_model=list[dict])
# async def get_bands_by_genre(genre: GenreChoice) -> list[dict]:
#     """
#     Endpoint to get all bands by genre.
#     """
#     genre_value = genre.value.lower()
#     filtered_bands = [
#         b for b in band if b["genre"].lower() == genre_value
#     ]
#     return filtered_bands


class GenreChoice(Enum):
    POP = 'pop'
    ROCK = 'rock'
    JAZZ = 'jazz'
    CLASSICAL = 'classical'

# class GenreChoice(str, Enum):
#     ROCK = 'rock'
#     POP = 'pop'
#     JAZZ = 'jazz'
#     CLASSICAL = 'classical'

    # @classmethod
    # def _missing_(cls, value):
    #     if isinstance(value, str):
    #         for member in cls:
    #             if member.value.lower() == value.lower():
    #                 return member
    #     return None

@app.get("/api/bands/genre/{genre}", response_model=list[dict])
async def get_bands_by_genre(genre: GenreChoice) -> list[dict]:
    genre_value = genre.value.lower()
    filtered_bands = [
        b for b in band if b["genre"].lower() == genre_value
    ]
    return filtered_bands