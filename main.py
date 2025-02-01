from fastapi import FastAPI
from datetime import datetime
import pytz
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
@app.get("/")
def get_info():
    return {
        "email": "sumayashittu@gmail.com",
        "current_datetime": datetime.now(pytz.utc).isoformat(),
        "github_url": "https://github.com/Sumayahx/HNG-backend__001"
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"]
)