'''
Imprime todos los valores de la matriz junto con su posición (fila, columna)
'''

grid = [
    [2, 1, 0],
    [1, 1, 0],
    [0, 1, 2]
]

# rows = len(grid)
# cols = len(grid[0])

# for r in range(rows):
#     for c in range(cols):
#         print(f"({r}, {c}) - {grid[r][c]}")


'''
Para la celda (1, 1), imprime los valores de sus vecinos válidos
'''

rows = len(grid)
cols = len(grid[0])

def neighbors(r, c):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    valid = []
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            valid.append((nr, nc))
        
    return valid

for nr, nc in neighbors(1, 1):
    print(f"Vecino: ({nr}, {nc}) = {grid[nr][nc]}")
    
    
    
    