import streamlit as st

def main():
    st.title("Sistema Especialista para Compra de Carros")

    st.write("Bem-vindo ao sistema especialista para ajudar na decisão de compra de carros.")
    st.write("Responda às seguintes perguntas para obter uma recomendação.")

    # Coleta de dados do usuário
    idade = st.slider("Qual é a sua idade?", 18, 80)
    renda = st.slider("Qual é a sua renda mensal em reais?", 1000, 10000)
    marca = st.selectbox("Qual marca de carro você prefere?", ["Toyota", "Honda", "Ford", "Chevrolet"])
    estilo = st.selectbox("Que tipo de carro você prefere?", ["Sedan", "SUV", "Esportivo", "Hatchback"])

    # Defina as regras do sistema especialista
    recomendacao = recomendar_carro(idade, renda, marca, estilo)

    # Exiba a recomendação com base nas regras
    st.write(f"Com base nas suas respostas, recomendamos: {recomendacao}.")

def recomendar_carro(idade, renda, marca, estilo):
    if idade < 30 and renda > 5000 and marca == "Toyota" and estilo == "Sedan":
        return "Recomendamos o Toyota Corolla."
    elif idade < 40 and renda > 6000 and marca == "Honda" and estilo == "SUV":
        return "Recomendamos o Honda CR-V."
    elif idade < 50 and renda > 7000 and marca == "Ford" and estilo == "Esportivo":
        return "Recomendamos o Ford Mustang."
    else:
        return "Desculpe, não temos uma recomendação específica com base nas suas respostas."

if __name__ == "__main__":
    main()
