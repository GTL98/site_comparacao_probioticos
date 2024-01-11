# --- Importar as bibliotecas --- #
import os
from Bio import SeqIO
from json import load
import streamlit as st
from obter_seqs import obter_seqs
from gerar_grafico import gerar_grafico
from distancia_hamm import distancia_hamm
from obter_seq_probiotico import obter_seq_probiotico

# --- Configuração da página --- #
st.set_page_config(page_title='Novos Probióticos')

# --- Abrir o arquivo com os probióticos do banco de dados --- #
with open('probioticos_bd.txt', 'r') as txt:
    conteudo = txt.readlines()
    probioticos_bd = sorted([bacteria[:-1] for bacteria in conteudo])

# --- Criar a caixa de seleção com  as bactérias probióticas do banco de dados --- #
probioticos = st.selectbox(
    label='Escolha uma bactéria:',
    options=probioticos_bd,
    placeholder='Selecione uma bactéria',
    index=None
)

# --- Ler os arquivos FASTA e ver em quais cluster a bactéria está --- #
arquivos_fasta = []
for arquivo in os.listdir('./probioticos_50'):
    for registro in SeqIO.parse(f'./probioticos_50/{arquivo}', 'fasta'):
        if probioticos is not None:
            if probioticos in registro.description:
                if arquivo not in arquivos_fasta:
                    cluster = arquivo.split('_')[1].split('.')[0].strip()
                    arquivos_fasta.append(cluster)

# --- Abrir o arquivo JSON --- #
with open('indices_clusters.json', 'r', encoding='utf-8') as doc:
    dados_json = load(doc)

# --- Colocar qual a função junto com o cluster --- #
lista_clusters = []
for arquivo in arquivos_fasta:
    item = f'{dados_json[arquivo]} - {arquivo}'
    if item not in lista_clusters:
        lista_clusters.append(item)

# --- Criar uma lista com os clusters em que o probiótico está --- #
# lista_clusters = sorted([int(cluster) for cluster in arquivos_fasta])
clusters = st.selectbox(
    label='Escolha um cluster:',
    options=sorted(lista_clusters),
    placeholder='Selecione um cluster',
    index=None
)

# --- Armazenar em uma variável o dicionário com as sequências --- #
dic_seqs = obter_seqs(clusters, probioticos)

# --- Armazenar em uma variável o dicionário com a sequência do probiótico escolhido --- #
seq_probiotico = obter_seq_probiotico(clusters, probioticos)

# --- Criar um dicionário com as bactérias e o valor da distância de Hamming --- #
dic_distancia = {}

# --- Colocar no dicionário as bactérias e a sua distância de Hamming --- #
if dic_seqs is not None:
    for bacteria in dic_seqs:
        distancia = distancia_hamm(seq_probiotico, dic_seqs[bacteria])
        dic_distancia[bacteria] = distancia

# --- Criar uma lista com as distâncias de Hamming que será usada como intervalo para os gráficos --- #
lista_dis_hamm = [distancia for distancia in dic_distancia.values()]

# --- Criar o slider do intervalo --- #
if len(lista_dis_hamm) != 0:
    intervalo = st.slider(
        label='Escolha um intervalo:',
        min_value=min(lista_dis_hamm),
        max_value=max(lista_dis_hamm),
        value=(
            min(lista_dis_hamm),
            max(lista_dis_hamm)
        )
    )

    # --- Plotar o gráfico --- #
    gerar_grafico(
        intervalo[0],
        intervalo[1],
        dic_distancia
    )
