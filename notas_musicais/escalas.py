NOTAS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
ESCALAS = {'Maior': [0, 2, 4, 5, 7, 9, 11]}

def escalas(tonica, tonalidade) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tonica e uma tonalidade.

    Parameters:
        tonica (str): Tonica da escala.
        tonalidade (str): Tonalidade da escala.
    
    Returns:
        Um dicionario com as notas e os graus da escala.

    Examples:
        >>> escalas('C', 'Maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escalas('A', 'Maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    
    """
    intervalos = ESCALAS[tonalidade]
    tonica_pos = NOTAS.index(tonica)
    
    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % len(NOTAS)
        temp.append(NOTAS[nota])
    
    return {'notas': temp, 
            'graus':  ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}