# Music Recommendation App  

A simple Flask web application that recommends similar songs based on your input using a **Spotify dataset** and **cosine similarity**.  

##  Features  
- Enter a song name and get **recommended songs**.  
- Case-insensitive search (e.g., "shape of you" = "Shape Of You").  
- Works even with **partial song names** (e.g., "Shape" → finds "Shape of You").  
- Clean and responsive UI with a peaceful background.  

## 🛠️Tech Stack  
- **Python** (Flask, Pandas, Scikit-learn)  
- **HTML + CSS** for frontend  
- **Spotify Dataset** (CSV file with song features)  

## Project Structure  
music-recommendation-app/
│── app.py # Flask backend
│── recommend.py # Recommendation logic
│── SpotifyFeatures.csv # Dataset
│── templates/
│ └── index.html # Frontend HTML
│── static/
│ └── style.css # CSS styling
│── README.md # Project documentation
