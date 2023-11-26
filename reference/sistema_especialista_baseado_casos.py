import streamlit as st

def main():
    st.title("Sistema Especialista Baseado em Casos para Diagnóstico Médico")

    st.write("Bem-vindo ao sistema especialista para diagnóstico médico. Informe seus sintomas para receber um diagnóstico.")

    # Coleta de dados do usuário
    sintomas = st.multiselect("Selecione seus sintomas:", [
        "Febre",
        "Dor de cabeça",
        "Dor de garganta",
        "Tosse",
        "Fadiga",
        "Dor nas articulações",
    ])

    # Crie uma lista de casos (sintomas e diagnósticos correspondentes)
    casos = [
        (["Febre", "Dor de cabeça", "Dor de garganta", "Tosse"], "Resfriado"),
        (["Febre", "Dor de cabeça", "Dor de garganta", "Tosse", "Fadiga"], "Gripe"),
        (["Dor de cabeça", "Dor nas articulações"], "Dengue"),
        (["Dor de garganta", "Tosse", "Fadiga"], "Amigdalite"),
        (["Febre", "Dor de cabeça"], "Enxaqueca"),
    ]

    # Realize a correspondência de casos
    diagnostico = diagnosticar_doenca(sintomas, casos)

    # Exiba o diagnóstico
    if diagnostico:
        st.write(f"Com base nos sintomas informados, você pode ter {diagnostico}.")
    else:
        st.write("Desculpe, não conseguimos fazer um diagnóstico com base nos sintomas fornecidos.")

def diagnosticar_doenca(sintomas, casos):
    for caso in casos:
        sintomas_caso, doenca = caso
        #verifica se os sintomas informados pelo usuário correspondem a algum dos casos e
        # fornece um diagnóstico com base nessa correspondência.
        if set(sintomas).issubset(set(sintomas_caso)):
            return doenca
    return None

if __name__ == "__main__":
    main()
