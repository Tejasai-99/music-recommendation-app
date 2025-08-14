import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import random

# Load dataset
data = pd.read_csv("SpotifyFeatures.csv")  # Change to your file name

# Select only numeric features for scaling
numeric_features = data.select_dtypes(include=['number'])
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_features)

def recommend(song_name, top_n=5):
    # Convert input to lowercase
    song_name = song_name.lower()
    track_names = data['track_name'].str.lower()

    # Find all matches (partial or full)
    matches = data[track_names.str.contains(song_name, na=False)]

    if not matches.empty:
        # Take first match if multiple
        idx = matches.index[0]

        # Compute similarity for this song only
        similarity_scores = cosine_similarity(
            [scaled_data[idx]], scaled_data
        )[0]

        # Get top N similar songs (excluding itself)
        similar_indices = similarity_scores.argsort()[-top_n-1:-1][::-1]

        return data.iloc[similar_indices]['track_name'].tolist()
    else:
        # If no match, return random songs
        return data['track_name'].sample(top_n).tolist()


# Test
if __name__ == "__main__":
    results = recommend("Shape of You", top_n=5)
    print(results)
