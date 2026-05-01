from fastapi import FastAPI
from src.api.predict import router as predict_router
import uvicorn

app = FastAPI()
app.include_router(predict_router)

if __name__ == "__main__":
    uvicorn.run(app, port=3000)
    