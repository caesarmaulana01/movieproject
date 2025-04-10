import os
import json
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieproject.settings')
django.setup()

from movies.models import Movie, MpaaRating

with open('movies.json') as f:
    data = json.load(f)

for item in data:
    rating, created = MpaaRating.objects.get_or_create(
        type=item["mpaaRating"]["type"],
        label=item["mpaaRating"]["label"]
    )
    Movie.objects.create(
        name=item["name"],
        description=item["description"],
        img_path=item["imgPath"],  # Changed from imgPath
        duration=item["duration"],
        genre=item["genre"],
        language=item["language"],
        mpaa_rating=rating,  # Changed from mpaaRating
        user_rating=int(item["userRating"])  # Changed from userRating
    )
