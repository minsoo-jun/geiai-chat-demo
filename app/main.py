# main.py
# gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/genai-api
# gcloud run deploy genai-api --image gcr.io/$GOOGLE_CLOUD_PROJECT/genai-api --platform managed --region us-central1 --port=8080 --allow-unauthenticated
# IAM - Service Account - Role: Vertex AI サービス エージェント

from typing import Union

from fastapi import FastAPI
#from fastapi.responses import HTMLResponse
import vertexai
from vertexai.language_models import TextGenerationModel

app = FastAPI()

@app.get("/")
def read_root(q: str):
    if q == "" :
        return ""

    vertexai.init(project="ornate-time-399706", location="us-central1")
    parameters = {
        #"candidate_count": 1,
        "max_output_tokens": 256,
        "temperature": 0.2,
        "top_p": 0.8,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict("\"" + q + "\"",**parameters)
    #print(f"Response from Model: {response.text}")    
    return f"Response from Model: {response.text}"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

