# --- Importar a biblioteca --- #
import streamlit as st


def gerar_grafico_hamm_aa(
        min_dis: int,
        max_dis: int,
        dados: dict,
        tamanho_seq: int,
        tipo: str
):
    """
    Função responsável por mostrar o intervalo do gráfico.
    :param min_dis: Distância de Hamming mínima do cluster.
    :param max_dis: Distância de Hamming máxima do cluster.
    :param dados: Dicionário com as bactérias e distâncias de Hamming.
    :param tamanho_seq: Tamanho da sequência do probiótico.
    :param tipo: Tipo de análise (Absoluto ou Porcentagem).
    """
    if tipo == 'Absoluto':
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

        # --- Colocar em ordem crescente os valores --- #
        lista_ordenada = sorted([distancia for distancia in dic_intervalo.values()])

        # --- Mostrar quais são as bactérias e a distância de Hamming --- #
        for valor in lista_ordenada:
            for bacteria, distancia in dic_intervalo.items():
                if distancia == valor:
                    st.write(f'{bacteria.split("_")[1].strip()}: {distancia}')

    if tipo == 'Porcentagem':
        # --- Criar o dicionário com as bactérias que possuem a distância de Hamming em porcentagem --- #
        dic_intervalo = {}

        # --- Verificar se a distância de Hamming pertence ao intervalo --- #
        for bacteria, dist_hamm in dados.items():
            if min_dis <= dist_hamm <= max_dis:
                porc_hamm = round((dist_hamm / tamanho_seq) * 100, 2)
                dic_intervalo[bacteria] = porc_hamm

        # --- Gerar e plotar o gráfico com os dados que pertecem ao intervalo --- #
        st.bar_chart(dic_intervalo)

        # --- Mostrar quantas bactérias possui nesse intervalo --- #
        st.header(
            f'Total de bactérias: {len(dic_intervalo.keys())}',
            divider='rainbow'
        )

        # --- Colocar em ordem crescente os valores --- #
        lista_ordenada = sorted([distancia for distancia in dic_intervalo.values()])

        # --- Mostrar quais são as bactérias e a porcentagem --- #
        for valor in lista_ordenada:
            for bacteria, porcentagem in dic_intervalo.items():
                if porcentagem == valor:
                    st.write(f'{bacteria.split("_")[1].strip()}: {porcentagem} %')
