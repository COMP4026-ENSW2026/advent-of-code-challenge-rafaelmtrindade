from sys import stdin


root = {}
pwd = []
dir_sizes = []


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
        return
    id, name = line.split()
    get_cwd()[name] = {} if id == 'dir' else int(id)


def get_tree_size(dir_tree: dict) -> int:
    total_size = 0
    for value in dir_tree.values():
        total_size += value if isinstance(value, int) else get_tree_size(value)
    dir_sizes.append(total_size)
    return total_size


def bin_usearch(arr: "list[int]", x: int) -> int:
    if arr[-1] < x:
        return None

    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

for line in stdin:
    parse_line(line)

# 70MB: Total do sistema; 30MB: Espaço necessário
min_dir_size = get_tree_size(root) + 30_000_000 - 70_000_000
dir_sizes.sort()
sel_dir_size = dir_sizes[bin_usearch(dir_sizes, min_dir_size)]

print('Tamanho da menor pasta que pode ser removida:', sel_dir_size, 'bytes')
