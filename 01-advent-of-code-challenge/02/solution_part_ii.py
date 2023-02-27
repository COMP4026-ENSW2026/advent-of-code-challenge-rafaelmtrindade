from sys import stdin

def get_score(i, j):
    '''
    |   | X | Y | Z |
    | - | - | - | - |
    | A | 3 | 1 | 2 |
    | B | 1 | 2 | 3 |
    | C | 2 | 3 | 1 |

    X: Derrota - +0pts
    Y: Empate - +3pts
    Z: Vitória - +6pts

    M[i][j]:
        i: escolha do adversário
        j: resultado desejado para o round
    '''
    M = [
        [3, 1, 2],
        [1, 2, 3],
        [2, 3, 1]
    ]
    return M[i][j] + 3*j


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
