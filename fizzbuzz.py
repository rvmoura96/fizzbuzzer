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


def assert_equal(result, expected):
    from sys import _getframe
    message = 'Fail: Line {} got {} expecting {}'

    if not result == expected:
        current = _getframe()
        caller = current.f_back
        line_num = caller.f_lineno
        print(message.format(line_num, result, expected))


if __name__ == '__main__':
    assert_equal(robot(1), '1')
    assert_equal(robot(2), '2')
    assert_equal(robot(4), '4')

    assert_equal(robot(3), 'fizz')
    assert_equal(robot(6), 'fizz')
    assert_equal(robot(9), 'fizz')

    assert_equal(robot(5), 'buzz')
    assert_equal(robot(10), 'buzz')
    assert_equal(robot(20), 'buzz')

    assert_equal(robot(15), 'fizzbuzz')
    assert_equal(robot(30), 'fizzbuzz')
    assert_equal(robot(45), 'fizzbuzz')
