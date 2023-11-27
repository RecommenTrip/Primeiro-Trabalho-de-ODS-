import streamlit as st

user_info = {
    "nome": "",
    "idade": 0,
    "q1": 0,
    "q2": 0,
    "q3": 0,
    "q4": 0,
    "q5": 0,
    "q6": 0,
    "q7": 0
}

def recommend_app():
    st.title("Sistema de Recomendação Colaborativo de Música")

    st.write("Bem-vindo ao sistema inteligente que irá te ajudar na decisão da sua próxima viagem!")

    st.write("Dados pessoais: ")

    user_info["nome"] = st.text_input("Digite o nome de usuário:")
    user_info["idade"] = st.slider("Qual é a sua idade?", 18, 80)

    st.write("Responda às seguintes perguntas para obter uma recomendação: ")

    user_info["q1"] = st.slider("Você gosta de praias?", 0, 5)
    user_info["q2"] = st.slider("O quanto cidades grandes te atraem?", 0, 5)
    user_info["q3"] = st.slider("Qual a temperatura ideal para o seu destino? (0) -> Frio | (1) -> Calor", 0, 5)
    user_info["q4"] = st.slider("Você gosta de cidades populosas?", 0, 5)
    user_info["q5"] = st.slider("Prefere viagens de aventura ou destinos mais relaxantes?", 0, 5)
    user_info["q6"] = st.slider("Gosta de visitar lugares históricos?", 0, 5)
    user_info["q7"] = st.slider("Tem interesse por turismo religioso?", 0, 5)

    if st.button("Salvar Preferências"):
        print("Salvar!")


# Função principal do aplicativo Streamlit
def main():
    recommend_app()

if __name__ == "__main__":
    main()