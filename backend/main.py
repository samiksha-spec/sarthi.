from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS (Allow requests from frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:3000"] for stricter access
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class TextInput(BaseModel):
    text: str

# Mock-based emotion analysis
@app.post("/analyze")
async def analyze_emotion(data: TextInput):
    text = data.text.lower()

    if any(word in text for word in ["happy", "excited", "joy", "glad"]):
        return {"emotion": "Happy 😊", "confidence": 0.95}
    elif any(word in text for word in ["sad", "down", "unhappy", "depressed"]):
        return {"emotion": "Sad 😢", "confidence": 0.92}
    elif any(word in text for word in ["angry", "mad", "furious"]):
        return {"emotion": "Angry 😠", "confidence": 0.90}
    elif any(word in text for word in ["nervous", "worried", "anxious", "scared"]):
        return {"emotion": "Anxious 😟", "confidence": 0.88}
    else:
        return {"emotion": "Neutral 😐", "confidence": 0.70}
