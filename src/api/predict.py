from fastapi import APIRouter, UploadFile, File, Request
import os
from src.predictor import Predictor

router = APIRouter()

UPLOAD_DIR = "uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)
preedictor = Predictor()

@router.post("/predict-image/")
async def predict_image(request: Request, file: UploadFile = File(...)):
    
    # 1️⃣ Save image
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)

    # 2️⃣ Get model from app state
    predictor = preedictor.predict_image(img_path=file_path)

    # 3️⃣ Predict
    result = predictor

    return {
        "filename": file.filename,
        "prediction": result
    }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(router, port=8000)