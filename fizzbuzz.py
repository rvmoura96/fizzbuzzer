u"""Regras do Fizzbuzz.

1. Se a posição for múltipla de 3: fizz
2. Se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: Fizzbuzz
4. Para qualquer outra posição fale o próprio nº.
"""

from functools import partial


def multiple_of(base, number):
    """Funcao responsavel pela verificacao se um numero x e multiplo de y.

    Sendo:
        x => number
        y => base

    """
    return number % base == 0


multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)


def robot(position):
    """Funcao responsavel pela execucao das regras do Fizzbuzz."""
    say = str(position)

    if multiple_of_3(position) and multiple_of_5(position):
        say = 'fizzbuzz'
    elif multiple_of_5(position):
        say = 'buzz'
    elif multiple_of_3(position):
        say = 'fizz'

    return say


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'
    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'
    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'
    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'
