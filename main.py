from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Note(BaseModel):
    content: str

@app.post("/summarize")
def summarize(note: Note):
    return {"summary": "This is a fake summary of: " + note.content}
