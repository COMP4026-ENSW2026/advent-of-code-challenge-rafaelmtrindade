from sys import stdin


def get_char_value(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    return ord(c) - ord('A') + 27


total = 0
for line in stdin:
    l = len(line)
    cmpart_a, cmpart_b = line[:l//2], line[l//2:]

    while cmpart_a:
        if cmpart_a[0] in cmpart_b:
            total += get_char_value(cmpart_a[0])
            break
        cmpart_a = cmpart_a.replace(cmpart_a[0], '')

print(f'Soma das prioridades: {total}')
