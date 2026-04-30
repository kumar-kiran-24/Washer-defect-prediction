from fastapi import FastAPI,File,UploadFile
from pydantic import BaseModel
import uvicorn
from predictor import Predictor

app = FastAPI()



@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    # Read image content
    contents = await file.read()
    path=f"uploaded_images/{file.filename}"
    file_location = f"uploaded_images/{file.filename}"
    with open(file_location, "wb") as f:    \
        f.write(contents)
    return {"filename": file.filename}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)