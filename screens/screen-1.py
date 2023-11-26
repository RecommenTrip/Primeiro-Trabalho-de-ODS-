import streamlit as st


def recommend_app():
    st.title("Sistema de Recomendação Colaborativo de Música")

    st.write("Bem-vindo ao sistema inteligente que irá te ajudar na decisão da sua próxima viagem!")
    st.write("Responda às seguintes perguntas para obter uma recomendação.")

    username = st.text_input("Digite o nome de usuário:")
    idade = st.slider("Qual é a sua idade?", 18, 80)
    qst_01 = st.slider("Você gosta de praias?", 0, 5)
    qst_02 = st.slider("O quanto cidades grandes te atraem?", 0, 5)
    qst_03 = st.slider("Qual a temperatura ideal para o seu destino?", 0, 5)
    qst_04 = st.slider("Você gosta de cidades populosas?", 0, 5)
    qst_05 = st.slider("Prefere viagens de aventura ou destinos mais relaxantes?", 0, 5)
    qst_06 = st.slider("Gosta de visitar lugares históricos?", 0, 5)
    qst_07 = st.slider("Tem interesse por turismo religioso?", 0, 5)


    st.write(f"Nome: {username}.")
    st.write(f"Idade: {idade}.")

    st.write(f"Questão 1): {qst_01}.")
    st.write(f"Questão 2): {qst_02}.")
    st.write(f"Questão 3=: {qst_03}.")
    st.write(f"Questão 4): {qst_04}.")
    st.write(f"Questão 5): {qst_05}.")
    st.write(f"Questão 6): {qst_06}.")
    st.write(f"Questão 7): {qst_07}.")


# Função principal do aplicativo Streamlit
def main():
    print("Teste")
    recommend_app()

if __name__ == "__main__":
    main()