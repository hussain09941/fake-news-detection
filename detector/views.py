import os
import pickle

from django.conf import settings
from django.shortcuts import render


# Load model paths
model_path = os.path.join(
    settings.BASE_DIR,
    "model",
    "fake_news_model.pkl"
)

vectorizer_path = os.path.join(
    settings.BASE_DIR,
    "model",
    "vectorizer.pkl"
)


# Load trained model
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Load TF-IDF vectorizer
with open(vectorizer_path, "rb") as file:
    vectorizer = pickle.load(file)


def home(request):
    prediction = None
    confidence = None

    if request.method == "POST":
        news = request.POST.get("news")

        # Convert text to TF-IDF
        news_tfidf = vectorizer.transform([news])

        # Predict
        result = model.predict(news_tfidf)[0]

        # Get probability
        probability = model.predict_proba(news_tfidf)[0]

        if result == 0:
            prediction = "FAKE NEWS "
            confidence = probability[0] * 100
        else:
            prediction = "REAL NEWS "
            confidence = probability[1] * 100

    return render(
        request,
        "home.html",
        {
            "prediction": prediction,
            "confidence": confidence,
        }
    )