import streamlit as st
from math import sqrt
import uuid
from streamlit_card import card

def create_card(title, image):
   unique_key = generate_unique_key()
   hasClicked = card(
        title=title,
        text="Compre agora!",
        key=unique_key,
        image=image,
        on_click=lambda: print("Clicked"),
        styles={
            "card": {
                "width": "100%",
                "height": "100px",
                "border-radius": "10px", 
                "position": "relative", 
                "padding": "20px",  
                "background-color": "#add8e6",
                "margin-bottom": "0px",
                "margin-top": "0px"
            }
        }
    )

       

def generate_unique_key():
    return str(uuid.uuid4())


def recommend():
    places_to_visit = [
        ("Paris", "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?q=80&w=2073&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"),
        ("Roma", "https://images.unsplash.com/photo-1552832230-c0197dd311b5?q=80&w=1996&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"),
        ("Londres", "https://images.unsplash.com/photo-1533929736458-ca588d08c8be?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"),
        ("Tóquio", "https://images.unsplash.com/photo-1533050487297-09b450131914?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"),
        ("Nova York", "https://images.unsplash.com/photo-1492666673288-3c4b4576ad9a?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
    ]
    return places_to_visit

# Função para criar o aplicativo Streamlit
def recommend_app():
    st.title("Recommentrip te sugere os seguintes locais:")

    recommendations = recommend()
    
    for recommendation in recommendations:
        create_card(f"{recommendation[0]}", recommendation[1])
        

# Função principal do aplicativo Streamlit
def main():
    recommend_app()

if __name__ == "__main__":
    main()
