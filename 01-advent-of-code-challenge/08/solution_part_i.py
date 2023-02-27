from sys import stdin


tree_grid = []
n_hidden = 0


for line in stdin:
    tree_grid.append(list(map(int, line.strip()[:])))

for i, row in enumerate(tree_grid[1:-1], start=1):
    for j, col in enumerate(row[1:-1], start=1):
        if max(row[:j]) < col: continue # left
        if max([u_row[j] for u_row in tree_grid[:i]]) < col: continue # top
        if max(row[j+1:]) < col: continue # right
        if max([d_row[j] for d_row in tree_grid[i+1:]]) < col: continue # bottom
        n_hidden += 1

print('Árvores visíveis:', len(tree_grid) * len(tree_grid[0]) - n_hidden)