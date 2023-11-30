import streamlit as st
import sys
import os
import random
from unidecode import unidecode
from fuzzywuzzy import fuzz

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from services.place_service import PlaceService


place_serv = PlaceService('http://127.0.0.1:5000/recommendation_places')

def read_city_image_urls(file_path):
    city_image_urls = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) >= 2:
                city = parts[0].strip()
                url = parts[1].strip()
                city_image_urls[city] = url
    return city_image_urls

def read_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    return [unidecode(line.strip()) for line in lines]

recommended_places = read_file('common/recommended_places.txt')
city_image_urls = read_city_image_urls('common/city_image_urls.txt')


places_with_images = []

for place in recommended_places:
    max_similarity = 0
    matching_city = None
    for city in city_image_urls.keys():
        similarity = fuzz.partial_ratio(place.lower(), city.lower())
        if similarity > max_similarity:
            max_similarity = similarity
            matching_city = city
    if matching_city:
        places_with_images.append((place, city_image_urls[matching_city]))

def create_card(title, image):
    st.markdown("""
    <style>
    div.stColumn {
        padding: 20px 500px; /* Experimente com valores para o padding */
    }
    </style>
""", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 8])
    with col1:
      st.image(image, use_column_width='auto')
    with col2:
        if st.button(f"Compre agora! - {title}"):

            recommended_places = place_serv.send_data(title)['data']
            recommended_places = random.sample(recommended_places, 5)
            print(f"Esses são os locais 2: {recommended_places}")

            directory = "common"
            if not os.path.exists(directory):
                os.makedirs(directory)
            with open(os.path.join(directory, 'recommended_places.txt'), 'w') as f:
                for item in recommended_places:
                    f.write("%s\n" % item)


def main():
    st.markdown("<h1 style='text-align: center;'>Recommentrip te sugere os seguintes locais:</h1>", unsafe_allow_html=True)
    
    for place, image_url in places_with_images:
        create_card(place, image_url)

if __name__ == "__main__":
    main()
