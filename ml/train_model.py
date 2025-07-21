import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
df = pd.read_csv("data/tasks_dataset.csv")

# Create pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])

# Train model
model.fit(df["task"], df["category"])

# Save model
joblib.dump(model, "ml/model.pkl")
print("✅ Model trained and saved to ml/model.pkl")
