gcloud builds submit \
  --tag gcr.io/$GOOGLE_CLOUD_PROJECT/genai-chat-api

gcloud run deploy genai-chat-api \
  --image gcr.io/$GOOGLE_CLOUD_PROJECT/genai-chat-api \
  --platform managed \
  --region us-central1 \
  --port=8080 \
  --allow-unauthenticated
