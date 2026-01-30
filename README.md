Movie Recommendation System
This project implements a content-based movie recommendation system using TF-IDF and cosine similarity.

Features
- Reads and cleans movie genres
- Converts text to TF-IDF vectors
- Computes cosine similarity
- Recommends similar movies
- CLI and Streamlit web interface

Tech Stack
- Python
- Pandas
- Scikit-learn
- NumPy
- Joblib
- Streamlit

## How to Run

### Mac / Linux
```bash
./run.sh

## Windows (PowerShell)
bash run.sh

If you prefer, you can also manually activate the virtual environment on Windows:

.venv\Scripts\activate
pip install -r requirements.txt
python -m streamlit run app/web_app.py
