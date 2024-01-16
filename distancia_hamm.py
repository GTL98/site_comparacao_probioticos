def distancia_hamm(seq_1: object, seq_2: object) -> int:
    """
    Função responsável por retornar a distância de Hamming entre as sequências sem respeitar
    as características fisico-químicas dos aminoácidos, somente os mismatches.
    :param seq_1: Sequência 1.
    :param seq_2: Sequência 2.
    :return: Distância de Hamming entre as sequências de aminoácidos.
    """
    # --- Distância de Hamming --- #
    distancia = 0

    # --- Calcular a distância de Hamming --- #
    for aa_1, aa_2, in zip(str(seq_1), str(seq_2)):
        if aa_1 != aa_2:
            distancia += 1

    return distancia
