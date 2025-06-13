from flask import Flask, request, Response
import numpy as np
import pandas as pd
import pickle
import json
import os

# Setup
app = Flask(__name__)
df = pd.read_csv("processed_venues.csv")

with open("similarity_matrix.pkl", "rb") as f:
    similarity_matrix = pickle.load(f)

def get_similar_venues_multi(venue_ids, top_n=5, same_city=True):
    weights = [0.5, 0.25, 0.1]  # Example: most recent to oldest
    weights = weights[:len(venue_ids)]
    weights = weights[::-1]  # Reverse to match order if newest is last

    sims = np.zeros(similarity_matrix.shape[1])
    total_weight = 0

    for i, v_id in enumerate(venue_ids):
        weight = weights[i] if i < len(weights) else 1  # fallback to 1 if not enough weights
        sims += similarity_matrix[v_id] * weight
        total_weight += weight

    sims /= total_weight  # Normalize

    for v_id in venue_ids:
        sims[v_id] = -1  # Exclude already viewed venues

    sim_scores = list(enumerate(sims))

    if same_city:
        target_city = df.iloc[venue_ids[-1]]["location"]  # assume newest viewed is last
        sim_scores = [
            (i, score) for i, score in sim_scores
            if df.iloc[i]["location"] == target_city
        ]

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    return sim_scores[:top_n]

@app.route("/recommend", methods=["GET"])
def recommend():
    try:
        ids_param = request.args.get("ids")
        id_param = request.args.get("id")
        top_n = int(request.args.get("n", 5))
        same_city = request.args.get("same_city", "true").lower() == "true"

        if ids_param:
            venue_ids = [int(i) for i in ids_param.split(",") if i.isdigit()]
            sim_scores = get_similar_venues_multi(venue_ids, top_n, same_city)
        elif id_param:
            venue_id = int(id_param)
            sim_scores = get_similar_venues_multi([venue_id], top_n, same_city)
        else:
            return Response(json.dumps({"error": "No venue ID(s) provided."}, ensure_ascii=False),
                content_type="application/json")

        results = [{
            "id": int(i),
            "name": df.iloc[i]["name"],
            "location": df.iloc[i]["location"],
            "tags": df.iloc[i]["tags"].split("|") if pd.notnull(df.iloc[i]["tags"]) else [],
            "type": df.iloc[i]["type"].split("|") if pd.notnull(df.iloc[i]["type"]) else [],
            "score": round(score, 2)
        } for i, score in sim_scores]

        return Response(
            json.dumps(results, ensure_ascii=False, indent=2),
            content_type="application/json; charset=utf-8"
        )
    except Exception as e:
        return Response(
            json.dumps({"error": str(e)}, ensure_ascii=False),
            content_type="application/json"
        )

def handler(request):
    with app.test_request_context(
        path=request.path,
        method=request.method,
        headers=dict(request.headers),
        data=request.body
    ):
        return recommend()

if __name__ == "__main__":
    app.run(debug=True)
