from sys import stdin


def get_score(i, j):
    '''
    Vitória: 6pts
    Empate: 3pts
    Derrota: 0pts

    |   | X | Y | Z |
    | - | - | - | - |
    | A | 3 | 6 | 0 |
    | B | 0 | 3 | 6 |
    | C | 6 | 0 | 3 |

    Pedra: +1pt
    Papel: +2pts
    Tesoura: +3pts

    M[i][j]:
        - i: escolha do adversário
        - j: escolha do jogador
    '''
    M = [
        [3, 6, 0],
        [0, 3, 6],
        [6, 0, 3]
    ]

    return j+1 + M[i][j]


def get_char_index(c):
    '''
    A ou X -> 0
    B ou Y -> 1
    C ou Z -> 2
    '''
    return (ord(c) - ord('A')) % 23


points = 0
for line in stdin:
    points += get_score(*map(get_char_index, line.split()))

print(f'Total: {points} pontos')
