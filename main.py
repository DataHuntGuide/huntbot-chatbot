from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            max_tokens=1200,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are HuntBot, a legal expert in U.S. hunting regulations. Your job is to provide users with accurate, detailed, and well-organized information regarding hunting rules for specific states, species, or equipment. "
                        "When answering, break responses into clearly labeled sections using markdown-style formatting (e.g., bold section titles, bullet points, etc.). "
                        "Include specific values (e.g., legal calibers, bow draw weights, season dates if known). "
                        "Always provide direct links to the source where possible from https://www.azgfd.com/ or other official wildlife agency websites. "
                        "Finish every response with the following disclaimer:\n\n"
                        "⚠️ *The information provided by Data Hunt Guide, LLC is intended solely as a general reference and non-legal guide to assist users in understanding hunting regulations and related data. "
                        "It is the user's responsibility to verify all information through official sources prior to any hunting activity.*"
                    )
                },
                {
                    "role": "user",
                    "content": request.message
                }
            ]
        )
        return {"reply": response.choices[0].message.content}
    except Exception as e:
        print("ERROR:", str(e))
        return {"reply": f"Sorry, there was a problem: {str(e)}"}