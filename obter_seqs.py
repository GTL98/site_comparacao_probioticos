# --- Importar a biblioteca --- #
from Bio import SeqIO


def obter_seqs(cluster: str, probiotico: str) -> dict:
    """
    Função responsável por obter as sequências dos arquivos FASTA do probiótico selecionado.
    :param cluster: Cluster selecionado.
    :param probiotico: Probiótico selecionado.
    :return: Dicionário com as sequências.
    """
    if cluster is not None:
        # --- Criar o dicionário que armazenara as sequências --- #
        dic_seq = {}

        # --- Ler o arquivo FASTA --- #
        contador = 0
        for registro in SeqIO.parse(f'./probioticos_50/Cluster_{cluster}.fasta', 'fasta'):
            if probiotico not in registro.description:
                bacteria = registro.description.split('[')[1][:-1].strip()
                dic_seq[f'{contador}_{bacteria}'] = registro.seq
                contador += 1

        return dic_seq
