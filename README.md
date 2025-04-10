# 🎬 Movie Listings @ GV Cinema

## 🎥 About the Project

A Django web application that displays a list of popular movies, complete with posters, details, and a live search feature. This project is designed to provide a seamless user experience with responsive layouts and visually appealing movie grids. It also includes features like custom image handling and a detailed movie information page.

--- 

## 🌟 Features

- ✅ List of movies with poster, name, duration, and user rating
- ✅ Detail page for each movie showing genre, language, duration, synopsis, and MPAA rating
- ✅ Live search bar to filter movies by name
- ✅ Responsive movie grid layout with consistent dimensions
- ✅ Static image loading from local assets
- ✅ Custom image zoom + center cropping to maintain visual symmetry

---

## 🖼️ Image Handling

- All images are stored locally under `movies/static/assets/images/`
- `imgPath` field in `movies.json` should follow this format:
```json
"imgPath": "assets/images/movie_poster.jpg"
```

In the template, paths are rendered like this:
```django
<img src="{% static movie.img_path|cut:'assets/' %}" alt="{{ movie.name }}">
```

## 🧑‍💻 Setup Instructions

1. Clone the Repository
```bash
git clone https://github.com/yourusername/movie-listing.git
cd movie-listing
```

2. Create Virtual Environment
```bash
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Run Migrations
```bash
python manage.py migrate
```

5. Load Movie Data
```bash
python manage.py load_movies
```

This custom Django command will load `movies.json` into your database.

6. Download Posters (Optional)

Make sure your `movies.json` file contains valid `"name"` and `"imgPath"` fields.
```bash
python download_image.py
```

This script will use Google Gemini API to fetch relevant movie posters and save them locally to match `imgPath`.


7. Run the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to:
```
http://127.0.0.1:8000/
```