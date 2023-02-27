from sys import stdin

cals_per_elf = [0]
curr_elf = 0
most_cals = 0

for line in stdin:
    try:
        val = int(line)
        cals_per_elf[curr_elf] += val
    except ValueError:
        if cals_per_elf[curr_elf] > most_cals:
            most_cals = cals_per_elf[curr_elf]
        cals_per_elf.append(0)
        curr_elf += 1

print(f'A maior quantidade de calorias que um elfo está carregando é {most_cals} cals')
