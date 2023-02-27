from sys import stdin


def get_char_value(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    return ord(c) - ord('A') + 27


total = 0
for line in stdin:
    elf_a, gp_inv = line.strip(), [input().strip() for _ in range(2)]
    while elf_a:
        if elf_a[0] in gp_inv[0] and elf_a[0] in gp_inv[1]:
            total += get_char_value(elf_a[0])
            break
        elf_a = elf_a.replace(elf_a[0], '')


print(f'Soma das prioridades: {total}')
