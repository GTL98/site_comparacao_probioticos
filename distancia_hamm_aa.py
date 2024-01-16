def distancia_hamm_aa(seq_1: object, seq_2: object) -> int:
    """
    Função responsável por retornar a distância de Hamming respeitando as características
    físico-químicas dos aminiácidos.
    :param seq_1: Sequência 1.
    :param seq_2: Sequência 2.
    :return: Distância de Hamming entre as sequências de aminoácidos.
    """
    # --- Dicionário com os aminoácidos e suas características físico-químicas --- #
    dic_aa = {
        'G': 'apolar',
        'L': 'apolar',
        'W': 'apolar',
        'A': 'apolar',
        'I': 'apolar',
        'M': 'apolar',
        'V': 'apolar',
        'F': 'apolar',
        'P': 'apolar',
        'D': 'ácido',
        'E': 'ácido',
        'K': 'básico',
        'R': 'básico',
        'H': 'básico',
        'S': 'polar',
        'T': 'polar',
        'C': 'polar',
        'N': 'polar',
        'Q': 'polar',
        'Y': 'polar'
    }

    # --- Distância de Hamming --- #
    distancia = 0

    # --- Calcular a distância de Hamming --- #
    for aa_1, aa_2, in zip(str(seq_1), str(seq_2)):
        if dic_aa[aa_1] != dic_aa[aa_2]:
            distancia += 1

    return distancia
