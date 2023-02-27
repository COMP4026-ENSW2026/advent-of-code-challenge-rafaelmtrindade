from sys import stdin


root = {}
pwd = []
total_u100kb = 0


def get_cwd() -> dict:
    cwd = root
    for dir in pwd[1:]:
        cwd = cwd[dir]
    return cwd


def parse_line(line: str):
    if line.startswith('$ ls'): return
    if line.startswith('$ cd'):
        tgt = line.split()[-1]
        pwd.pop() if tgt == '..' else pwd.append(tgt)
    elif line.startswith('dir'):
        dir_name = line.split()[-1]
        get_cwd()[dir_name] = {}
    else:
        file_size, file_name = line.split()
        get_cwd()[file_name] = int(file_size)


def add_total_u100kb(dir_tree: dict) -> int:
    global total_u100kb
    total_size = 0
    for value in dir_tree.values():
        total_size += value if isinstance(value, int) else add_total_u100kb(value)
    if total_size <= 100000:
        total_u100kb += total_size
    return total_size


for line in stdin:
    parse_line(line)
add_total_u100kb(root)

print(f'Total de bytes das pastas com menos de 100KB: {total_u100kb} bytes')
