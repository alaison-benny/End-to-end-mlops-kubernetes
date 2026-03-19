from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/predict")
def predict(text: str):
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return {"sentiment": "positive" if prediction == 1 else "negative"}

