from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Quantiva AI Backend is live!"}

@app.post("/scan")
async def scan_chart(file: UploadFile = File(...)):
    contents = await file.read()
    return {
        "status": "success",
        "prediction": "BUY",
        "confidence": 0.92
    }

@app.get("/qbot")
def ask_qbot(question: str):
    return {
        "question": question,
        "answer": "This is a smart response from QBot AI."
    }
