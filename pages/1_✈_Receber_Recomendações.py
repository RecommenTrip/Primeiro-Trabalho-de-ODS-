import streamlit as st
import sys
import os
import random

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from services.place_service import PlaceService


place_serv = PlaceService('http://127.0.0.1:5000/recommendation_places')

def read_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

recommended_places = read_file('common/recommended_places.txt')


places = [
    (recommended_places[0], "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?q=80&w=2073&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"),
    (recommended_places[1], "https://images.unsplash.com/photo-1552832230-c0197dd311b5?q=80&w=1996&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"),
    (recommended_places[2], "https://images.unsplash.com/photo-1533929736458-ca588d08c8be?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"),
    (recommended_places[3], "https://images.unsplash.com/photo-1533050487297-09b450131914?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"),
    (recommended_places[4], "https://images.unsplash.com/photo-1492666673288-3c4b4576ad9a?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
]

def create_card(title, image):
    col1, col2 = st.columns([2, 8])
    with col1:
        st.image(image, use_column_width=True)
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
    
    for place, image_url in places:
        create_card(place, image_url)

if __name__ == "__main__":
    main()
