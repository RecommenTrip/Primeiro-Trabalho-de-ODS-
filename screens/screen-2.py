import streamlit as st
from math import sqrt
import uuid
from streamlit_card import card


def create_card(title):
   unique_key = generate_unique_key()
   hasClicked = card(
        title=title,
        text="Compre agora!",
        key=unique_key,
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
        ("Paris", 9),
        ("Roma", 8),
        ("Londres", 9),
        ("Tóquio", 7),
        ("Nova York", 8)
    ]
    return places_to_visit

# Função para criar o aplicativo Streamlit
def recommend_app():
    st.title("Recommentrip te sugere os seguintes locais:")

    recommendations = recommend()
    
    for recommendation in recommendations:
        create_card(f"{recommendation[0]}")
        

# Função principal do aplicativo Streamlit
def main():
    recommend_app()

if __name__ == "__main__":
    main()
