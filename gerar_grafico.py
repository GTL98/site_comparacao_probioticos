# --- Importar a biblioteca --- #
import streamlit as st


def gerar_grafico(min_dis: int, max_dis: int, dados: dict):
    """
    Função responsável por mostrar o intervalo do gráfico.
    :param min_dis: Distância de Hamming mínima do cluster.
    :param max_dis: Distância de Hamming máxima do cluster.
    :param dados: Dicionário com as bactérias e distâncias de Hamming.
    """
    # --- Criar o dicionário com as bactérias que possuem a distância de Hamming dentro do intervalo --- #
    dic_intervalo = {}

    # --- Verificar se a distância de Hamming pertence ao intervalo --- #
    for bacteria, dist_hamm in dados.items():
        if min_dis <= dist_hamm <= max_dis:
            dic_intervalo[bacteria] = dist_hamm

    # --- Gerar e plotar o gráfico com os dados que pertecem ao intervalo --- #
    st.bar_chart(dic_intervalo)

    # --- Mostrar quantas bactérias possui nesse intervalo --- #
    st.header(
        f'Total de bactérias: {len(dic_intervalo.keys())}',
        divider='rainbow'
    )

    # --- Mostrar quais são as bactérias e a distância de Hamming --- #
    for bacteria, distancia in dic_intervalo.items():
        st.write(f'{bacteria}: {distancia}')
