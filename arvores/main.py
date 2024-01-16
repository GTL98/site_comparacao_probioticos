# --- Importar as bibliotecas --- #
import os
import time
from functools import wraps
from Bio.Align.Applications import ClustalOmegaCommandline


def memoize(funcao):
    cache = {}

    @wraps(funcao)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = funcao(*args, **kwargs)
        return cache[key]

    return wrapper


@memoize
def criar_arvores():
    # --- Caminho dos arquivos FASTA --- #
    caminho = '../geral/arquivos_sweep/'
    # --- Indicar o arquivo usado --- #
    lista_arquivos = [arquivo for arquivo in os.listdir(caminho)]

    # --- Informar o caminho do Clustal Omega --- #
    clustal_omega = r'C:\Users\bioinfo\Documents\ClustalOmega\clustalo.exe'

    # --- Fazer o alinhamento e a árvore --- #
    for arquivo in lista_arquivos:
        arquivo_arvore = f'{arquivo.replace(".fasta", "")}.tree'

        # --- Alinhamento e árvore do Clustal Omega --- #
        cline = ClustalOmegaCommandline(
            cmd=clustal_omega,
            infile=f'{caminho}/{arquivo}',
            guidetree_out=arquivo_arvore,
            force=True
        )

        # --- Gerar os arquivo de alinhamento e árvore --- #
        stdout, stderr = cline()


inicio = time.perf_counter()
criar_arvores()
final = time.perf_counter()
delta = round((final - inicio) / 60, 1)
print(f'O tempo de espera foi de {delta} minutos.')
