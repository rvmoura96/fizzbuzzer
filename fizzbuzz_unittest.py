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
