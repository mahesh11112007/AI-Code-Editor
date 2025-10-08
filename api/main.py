from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import openai
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

class CodeRequest(BaseModel):
    prompt: str
    language: str = "python"

class CodeResponse(BaseModel):
    code: str
    explanation: str

@app.get("/")
def root():
    return {"message": "AI Code Editor API is running"}

@app.post("/generate-code", response_model=CodeResponse)
async def generate_code(request: CodeRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful coding assistant. Generate {request.language} code based on the user's request. Provide both the code and a brief explanation."},
                {"role": "user", "content": request.prompt}
            ],
            max_tokens=1500
        )
        
        content = response.choices[0].message.content
        
        # Simple parsing to separate code and explanation
        if "```" in content:
            parts = content.split("```")
            code = parts[1].strip() if len(parts) > 1 else content
            explanation = parts[2].strip() if len(parts) > 2 else "Code generated successfully"
        else:
            code = content
            explanation = "Code generated successfully"
            
        return CodeResponse(code=code, explanation=explanation)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/explain-code")
async def explain_code(code: dict):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful coding assistant. Explain the provided code in simple terms."},
                {"role": "user", "content": f"Please explain this code: {code['code']}"}
            ],
            max_tokens=800
        )
        
        explanation = response.choices[0].message.content
        return {"explanation": explanation}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/optimize-code")
async def optimize_code(code: dict):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful coding assistant. Optimize the provided code for better performance, readability, and best practices."},
                {"role": "user", "content": f"Please optimize this code: {code['code']}"}
            ],
            max_tokens=1200
        )
        
        optimized_code = response.choices[0].message.content
        return {"optimized_code": optimized_code}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# For Vercel deployment
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
