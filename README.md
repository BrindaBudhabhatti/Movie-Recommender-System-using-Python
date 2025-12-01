# 🎬 Movie Recommender System

A simple **Content-Based Movie Recommendation System** built using **Python**, **Scikit-learn**, and **Streamlit**. This project takes a movie selected by the user and recommends the top 5 similar movies based on textual similarity.

---

## 🚀 Features

* Content-based filtering using **overview + genre**
* Text vectorization using **CountVectorizer**
* Similarity calculation using **Cosine Similarity**
* Interactive **Streamlit** web app
* Clean and minimal UI

---

## 📂 Project Structure

```
├── dataset.csv
├── movie-recommender.py
├── README.md
└── requirements.txt
```

---

## 📦 Installation

### **1. Clone the Repository**

```
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

### **2. Create Virtual Environment (optional)**

```
python -m venv env
source env/bin/activate      # Mac/Linux
env\Scripts\activate         # Windows
```

### **3. Install Dependencies**

```
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the Streamlit app:

```
streamlit run app.py
```

Then open the displayed local URL in your browser.

---

## 📘 How It Works

1. Load dataset
2. Combine *overview* and *genre* into a **tags** feature
3. Convert tags into numerical vectors using CountVectorizer
4. Use **cosine similarity** to compute closeness between movies
5. Display top 5 recommended movies in Streamlit

---

## 🧠 Technologies Used

* Python 3
* Pandas
* Scikit-learn
* Streamlit

---

## 📊 Example Screenshot

<img width="1919" height="1027" alt="image" src="https://github.com/user-attachments/assets/4b2a1736-bc0f-4f2d-b3c7-06a9b8cf9b25" />


---

## 📝 Future Improvements

* Use TF‑IDF Vectorizer
* Include metadata (actors, directors, keywords)
* Add posters using TMDB API
* Deploy online via Streamlit Cloud / Render / HuggingFace Spaces

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you want to change.

---

## 📄 License

This project is licensed under the **MIT License**.
