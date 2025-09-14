# 🎬 Bollywood Movie Recommender System

A simple and effective content-based recommendation system built using Python and machine learning that suggests similar Bollywood movies based on user input. Ideal for movie lovers looking for personalized suggestions!

## 🚀 Features

- 🔍 Content-based filtering using movie metadata (title, genres, cast, director)
- 📊 Uses cosine similarity to find and recommend similar movies
- 🧠 Built with popular Python libraries (Pandas, Scikit-learn)
- 🌐 Clean and interactive frontend (with Streamlit)
- 📁 Dataset: Bollywood movies dataset (from Kaggle)

---

## 📦 Tech Stack

- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Pickle
- **Model:** Cosine Similarity (Content-based Filtering)
- **Web Framework:** Streamlit 
- **IDE:** Jupyter Notebook / VS Code

---

---

## 🎯 How It Works

1. The dataset is cleaned and preprocessed (removing nulls, merging features).
2. A **combined feature column** is created using title, genre, cast, and director.
3. Text data is vectorized using **TF-IDF** or **CountVectorizer**.
4. **Cosine similarity** is used to compute similarity scores between movies.
5. When a user searches for a movie, the system returns top similar movies.
          ┌───────────────────────┐
          │   Import Dataset      │
          └─────────┬─────────────┘
                    │
          ┌─────────▼─────────────┐
          │   Data Preprocessing  │
          │ - Handle nulls        │
          │ - Clean text          │
          └─────────┬─────────────┘
                    │
          ┌─────────▼─────────────┐
          │  Feature Engineering  │
          │ - Combine columns     │
          │   (title, genres,     │
          │    cast, director)    │
          └─────────┬─────────────┘
                    │
          ┌─────────▼─────────────┐
          │ Vectorization (TF-IDF │
          │   or CountVectorizer)│
          └─────────┬─────────────┘
                    │
          ┌─────────▼─────────────┐
          │  Similarity Matrix    │
          │   (Cosine Similarity) │
          └─────────┬─────────────┘
                    │
          ┌─────────▼─────────────┐
          │   Recommendation Logic│
          │ - User inputs movie   │
          │ - Return top N similar│
          └─────────┬─────────────┘
                    │
          ┌─────────▼─────────────┐
          │   Frontend (optional) │
          │ - Streamlit or Flask  │
          └─────────┬─────────────┘
                    │
          ┌─────────▼─────────────┐
          │     Output UI/API     │
          │ - Show recommended    │
          │   Bollywood movies    │
          └───────────────────────┘


---

## 🛠️ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/pranayk15/Bollywood-Movie-Recommender.git
cd Bollywood-Movie-Recommender

# 2. Create a Virtual Environment
python -m venv venv
venv\Scripts\activate

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Run the app (if using Streamlit or Flask)
streamlit run app.py
# or
python app.py

