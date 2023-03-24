"""
    Arrange - Organizar
    Act - Agir
    Assert - Afirmar
"""
from pytest import raises, mark
from notas_musicais.escalas import escala, NOTAS, ESCALAS


def test_deve_funcionar_com_notas_minusculas():
    # Arrange
    tonica = 'c'
    tonalidade = 'maior'

    # Act - chama o que testaremos
    resultado = escala(tonica, tonalidade)

    # Assert - verifica se o resultado é o esperado
    assert resultado

def test_deve_retornar_um_erro_dizendo_que_a_nota_nao_existe():
    # Arrange
    tonica = 'X'
    tonalidade = 'maior'

    mensagem_de_erro = f'A nota não existe. tente uma dessas: {NOTAS}'

    with raises(ValueError) as error:
        escala(tonica, tonalidade)
    
    assert mensagem_de_erro == error.value.args[0]

def test_deve_retorna_um_erro_dizendo_que_a_escala_nao_existe():
    tonica = 'C'
    tonalidade = 'tonalidade'

    mensagem_de_erro = f'esta escala não existe, tente uma dessas: {list(ESCALAS.keys())}'

    with raises(KeyError) as error:
        escala(tonica, tonalidade)
    
    assert mensagem_de_erro == error.value.args[0]

@mark.parametrize(
        'tonica,esperado', 
        [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
         ],
        )
def test_deve_retornar_as_notas_corretas(tonica, esperado):
    resultado = escala(tonica, 'maior')
    assert resultado['notas'] == esperado

def test_deve_retornar_os_graus_corretos():
    resultado = escala('C', 'maior')
    assert resultado['graus'] == ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    