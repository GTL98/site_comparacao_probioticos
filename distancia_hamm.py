def distancia_hamm(seq_1: object, seq_2: object) -> int:
    """
    Função responsável por retornar a distância de Hamming entre as sequências.
    :param seq_1: Sequência 1.
    :param seq_2: Sequência 2.
    :return: Dicionário com a distância de Hamming entre as sequências.
    """
    # --- Distância de Hamming --- #
    distancia = 0

    # --- Calcular a distância de Hamming --- #
    for aa_1, aa_2, in zip(str(seq_1), str(seq_2)):
        if aa_1 != aa_2:
            distancia += 1

    return distancia
