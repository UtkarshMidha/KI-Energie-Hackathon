from fastapi import FastAPI
from src.api.routes import router
from dotenv import load_dotenv

load_dotenv()


app = FastAPI(title="PV Legal Advisor")
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


import os
from dotenv import load_dotenv

load_dotenv()

print("KEY FOUND:", bool(os.getenv("OPENAI_API_KEY")))
print("KEY PREFIX:", os.getenv("OPENAI_API_KEY", "")[:10])