import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load CSV
df = pd.read_csv("venues.csv")

# Build features column
df["features"] = (
    df["tags"].fillna("").str.replace("|", " ", regex=False) +
    df["type"].fillna("").str.replace("|", " ", regex=False) +
    df["location"].fillna("")
)

# TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["features"])

# Similarity matrix
similarity_matrix = cosine_similarity(tfidf_matrix)

# Save matrix and processed data
with open("similarity_matrix.pkl", "wb") as f:
    pickle.dump(similarity_matrix, f)

df.to_csv("processed_venues.csv", index=False)

print("Model and data saved successfully.")