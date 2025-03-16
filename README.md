Below is a detailed `README.md` file for your Movie Recommender System project, tailored for GitHub and your deployment on Streamlit Sharing. It includes an overview, setup instructions, usage details, file descriptions, and more.

---

# Movie Recommender System

This is a **Movie Recommender System** built using Python, Streamlit, and machine learning techniques. The system recommends movies based on content similarity using movie metadata such as genres, keywords, cast, crew, and overview. The recommendation engine leverages cosine similarity and is deployed as an interactive web application using Streamlit Sharing.

You can try the live app here: [[Streamlit Sharing Link](https://movie-recommender-system-ey7i4mgkxaryuiuow6dnde.streamlit.app/)].

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Deployment](#deployment)
- [Future Improvements](#future-improvements)

## Project Overview
The Movie Recommender System allows users to select a movie from a dropdown menu and receive five movie recommendations based on content similarity. It uses preprocessed movie data from the TMDB 5000 dataset and displays movie titles along with their posters fetched from The Movie Database (TMDb) API.

## Features
- **Movie Selection**: Choose a movie from a dropdown list of over 5000 movies.
- **Recommendations**: Get 5 similar movie recommendations based on content similarity.
- **Poster Display**: View movie posters alongside titles for a visually appealing experience.
- **Interactive UI**: Built with Streamlit for a simple and intuitive user interface.
- **Deployed Online**: Accessible via Streamlit Sharing.

## Technologies Used
- **Python**: Core programming language.
- **Pandas**: Data manipulation and preprocessing.
- **NumPy**: Numerical operations.
- **Scikit-learn**: Cosine similarity computation for recommendations.
- **NLTK**: Text preprocessing (stemming).
- **Streamlit**: Web app framework.
- **Requests**: API calls to fetch movie posters from TMDb.
- **Pickle**: Serialization of precomputed data.
- **TMDb API**: For fetching movie poster images.

## Dataset
The project uses the **TMDB 5000 Movie Dataset** available on Kaggle, which includes:
- `tmdb_5000_movies.csv`: Movie metadata (title, genres, keywords, overview, etc.).
- `tmdb_5000_credits.csv`: Credits data (cast and crew).

The dataset is preprocessed to create a recommendation system based on movie tags derived from genres, keywords, cast, crew, and overview.

## How It Works
1. **Data Preprocessing** (from the `.ipynb` file):
   - Merge movie and credits datasets.
   - Select relevant columns: `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, `crew`.
   - Clean data: Remove null values and duplicates.
   - Transform data:
     - Convert `genres` and `keywords` into lists of names.
     - Extract top 3 cast members and the director from `crew`.
     - Combine all features into a `tags` column.
     - Apply stemming (using NLTK's PorterStemmer) and lowercase transformation.
   - Vectorize `tags` using `CountVectorizer` (5000 max features, English stop words removed).
   - Compute cosine similarity between movie vectors.

2. **Recommendation Logic**:
   - Find the index of the selected movie.
   - Sort movies by similarity scores and return the top 5 (excluding the input movie).

3. **Web App**:
   - Load precomputed data (`movie_dict.pkl` and `similarity.pkl`).
   - Use Streamlit to create an interactive UI.
   - Fetch movie posters via the TMDb API.

## Installation
To run this project locally, follow these steps:

### Prerequisites
- Python 3.8+
- Git
- A TMDb API key (sign up at [The Movie Database](https://www.themoviedb.org/) to get one)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/RomanRybitskyi/movie-recommender-system.git
   cd movie-recommender-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your TMDb API key:
   - Replace the `api_key` value in the `fetch_poster` function in `Movie-Recommender-System.py` with your own key:
     ```python
     response = requests.get('https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US'.format(movie_id=movie_id))
     ```

4. Run the app:
   ```bash
   streamlit run Movie-Recommender-System.py
   ```

5. Open your browser and go to `http://localhost:8501`.

### Requirements
Create a `requirements.txt` file with the following:
```
streamlit
pandas
numpy
requests
nltk
scikit-learn
```

## Usage
1. Launch the app locally or visit the deployed version.
2. Select a movie from the dropdown menu.
3. Click the "Recommend" button.
4. View the 5 recommended movies with their titles and posters displayed in a 5-column layout.

## File Structure
```
movie-recommender-system/
├── Movie-Recommender-System.py             # Streamlit app code
├── movie_dict.pkl      # Pickled movie DataFrame
├── similarity.pkl      # Pickled similarity matrix
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```
*Note*: The `.ipynb` file is not included here but was used for data preprocessing and model creation.

## Deployment
The app is deployed on **Streamlit Sharing**. To deploy your own version:
1. Push your code to a public GitHub repository.
2. Sign up for Streamlit Sharing at [share.streamlit.io](https://share.streamlit.io/).
3. Link your repository and deploy the app with `Movie-Recommender-System.py` as the entry point.
4. Ensure `movie_dict.pkl`, `similarity.pkl`, and `requirements.txt` are included in the repository.

## Future Improvements
- Add user ratings to improve recommendations (collaborative filtering).
- Include more metadata (e.g., release year, runtime).
- Enhance UI with filters (e.g., by genre or year).
- Optimize performance for larger datasets.
- Add error handling for API failures.

