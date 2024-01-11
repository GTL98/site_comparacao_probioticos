# --- Importar a biblioteca --- #
from Bio import SeqIO


def obter_seq_probiotico(cluster: str, probiotico: str) -> object:
    """
    Função responsável por obter somente a sequência do probiótico selecionado.
    :param cluster: Cluster selecionado.
    :param probiotico: Probiótico selecionado.
    :return: Objeto Seq com a sequência do probiótico.
    """
    if cluster is not None:
        # --- Variável que receberá o objeto Seq --- #
        seq_probiotico = None

        # --- Tratar a entrada do cluster --- #
        cluster_numero = cluster.split('-')[1].strip()

        if cluster is not None:
            # --- Ler o arquivo FASTA --- #
            for registro in SeqIO.parse(f'./probioticos_50/Cluster_{cluster_numero}.fasta', 'fasta'):
                if probiotico in registro.description:
                    seq_probiotico = registro.seq

        return seq_probiotico
