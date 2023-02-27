from sys import stdin


def get_marker_index(stream, size):
    n = size - 1
    buffer = '_' + stream[:n]
    for i, c in enumerate(stream[n:]):
        buffer = buffer[1:] + c
        if len(set(buffer)) == size: return i + n


data_stream = stdin.readline()
print(f'Posição do marcador de mensagem: {get_marker_index(data_stream, 14) + 1}')