from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from backend.agent import generate_instagram_post
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()

class PostRequest(BaseModel):
    product_name : str
    features : str
    style_example: str
    
@app.post('/generate')
def generate_post(request: PostRequest):
    try:
        logger.info(f"Received request: {request}")
        result = generate_instagram_post(
            request.product_name,
            request.features,
            request.style_example
        )
        return {'result': result}
    except Exception as e:
        logger.error(f"Error in /generate: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "API is running"}

