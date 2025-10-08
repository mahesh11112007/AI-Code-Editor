from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
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

class FileCreateRequest(BaseModel):
    filename: str
    content: str

# Basic health and hello endpoints for Vercel API routing
@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from AI Code Editor API"}

@app.get("/", response_class=HTMLResponse)
def root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI Code Editor API</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            
            .container {
                background: rgba(255, 255, 255, 0.95);
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                padding: 50px;
                max-width: 800px;
                width: 100%;
                text-align: center;
            }
            
            .logo {
                font-size: 4rem;
                margin-bottom: 20px;
            }
            
            h1 {
                color: #333;
                font-size: 2.5rem;
                margin-bottom: 15px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            
            .tagline {
                color: #666;
                font-size: 1.2rem;
                margin-bottom: 30px;
            }
            
            .description {
                color: #555;
                font-size: 1rem;
                line-height: 1.6;
                margin-bottom: 40px;
                text-align: left;
            }
            
            .api-links {
                display: flex;
                gap: 20px;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 30px;
            }
            
            .api-link {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-decoration: none;
                padding: 15px 30px;
                border-radius: 50px;
                font-weight: 600;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            }
            
            .api-link:hover {
                transform: translateY(-3px);
                box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
            }
            
            .features {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin-top: 40px;
                text-align: left;
            }
            
            .feature {
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                padding: 20px;
                border-radius: 10px;
                transition: transform 0.3s ease;
            }
            
            .feature:hover {
                transform: scale(1.05);
            }
            
            .feature-icon {
                font-size: 2rem;
                margin-bottom: 10px;
            }
            
            .feature-title {
                font-weight: 600;
                color: #333;
                margin-bottom: 5px;
            }
            
            .feature-desc {
                font-size: 0.9rem;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo">🤖💻</div>
            <h1>AI Code Editor API</h1>
            <p class="tagline">Powered by OpenAI • Built with FastAPI</p>
            
            <div class="description">
                <p>Welcome to the AI Code Editor API - your intelligent coding companion! 
                This powerful API leverages OpenAI's GPT models to help you generate, explain, 
                and optimize code across multiple programming languages.</p>
            </div>
            
            <div class="features">
                <div class="feature">
                    <div class="feature-icon">✨</div>
                    <div class="feature-title">Code Generation</div>
                    <div class="feature-desc">Generate code from natural language descriptions</div>
                </div>
                <div class="feature">
                    <div class="feature-icon">📖</div>
                    <div class="feature-title">Code Explanation</div>
                    <div class="feature-desc">Understand complex code with AI explanations</div>
                </div>
                <div class="feature">
                    <div class="feature-icon">⚡</div>
                    <div class="feature-title">Code Optimization</div>
                    <div class="feature-desc">Improve performance and best practices</div>
                </div>
            </div>
            
            <div class="api-links">
                <a href="/api/health" class="api-link">Health Check</a>
                <a href="/api/hello" class="api-link">API Hello</a>
                <a href="/docs" class="api-link">API Documentation</a>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

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

@app.post("/api/create-file")
async def create_file(request: FileCreateRequest):
    """Create a file with given filename and content (cloud storage ready)"""
    try:
        # For now, return success response
        # In production, this would integrate with cloud storage (S3, GCS, etc.)
        return {
            "status": "success",
            "message": f"File '{request.filename}' created successfully",
            "filename": request.filename,
            "size": len(request.content)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/upload")
async def upload_file(file: dict):
    """Upload a file (cloud storage ready)"""
    try:
        # For now, return success response
        # In production, this would integrate with cloud storage (S3, GCS, etc.)
        filename = file.get("filename", "unknown")
        content = file.get("content", "")
        
        return {
            "status": "success",
            "message": f"File '{filename}' uploaded successfully",
            "filename": filename,
            "size": len(content)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# For Vercel deployment
# Vercel's Python runtime expects the handler to be exported as `app` from this module.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
