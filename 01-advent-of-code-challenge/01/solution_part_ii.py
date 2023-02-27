from sys import stdin

cals_per_elf = [0]
curr_elf = 0

for line in stdin:
    try:
        val = int(line)
        cals_per_elf[curr_elf] += val
    except ValueError:
        cals_per_elf.append(0)
        curr_elf += 1

cals_per_elf.sort(reverse=True)
print(f'Os três elfos carregando mais calorias possuem, juntos, {sum(cals_per_elf[:3])} cals')