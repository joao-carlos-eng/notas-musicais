NOTAS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
ESCALAS = {'maior': [0, 2, 4, 5, 7, 9, 11]}

def escala(tonica, tonalidade) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tonica e uma tonalidade.

    Parameters:
        tonica (str): Tonica da escala.
        tonalidade (str): Tonalidade da escala.
    
    Returns:
        Um dicionario com as notas e os graus da escala.

    Raises:
        ValueError: Caso a tonica passada não seja valida
        KeyError: Caso a tonalidade passada não seja valida
    
    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('a', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    
    """
    tonica = tonica.upper()
    try:
        intervalos = ESCALAS[tonalidade]
    except KeyError:
        raise KeyError(f'esta escala não existe, tente uma dessas: {list(ESCALAS.keys())}')
    
    try:
        tonica_pos = NOTAS.index(tonica)
    except ValueError:
        raise ValueError(f'A nota não existe. tente uma dessas: {NOTAS}')
    
    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % len(NOTAS)
        temp.append(NOTAS[nota])
    
    return {'notas': temp, 
            'graus':  ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}