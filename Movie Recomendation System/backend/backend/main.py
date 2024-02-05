# main.py
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from recommendations_logic import get_recommendations  # Import your recommendation logic

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/recommendations/{movie_name}")
async def get_movie_recommendations(movie_name: str ):
    try:
        # Use the get_recommendations function from your recommendation logic file
        recommendations = get_recommendations(movie_name)
        return JSONResponse(content={"recommendations": recommendations})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
