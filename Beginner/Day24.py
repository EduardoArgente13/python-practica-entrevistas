# grid = [
#     [2, 1, 1],
#     [1, 1, 0],
#     [0, 1, 1]
# ]

# for r in range(len(grid)):
#     for c in range(len(grid[0])):
#         print(f"En la posición ({r}, {c}) hay: {grid[r][c]}")


'''
Dado una matriz 2D grid que representa una caja de naranjas:
0: celda vacía
1: naranja fresca
2: naranja podrida

Cada minuto, una naranja podrida puede contagiar a las naranjas frescas adyacentes (arriba, abajo, izquierda, derecha).
Objetivo:
Devuelve el número mínimo de minutos necesarios para que todas las naranjas frescas se pudran.
Si es imposible, devuelve -1.
'''

from collections import deque

def orangesRotting(grid):
    if not grid:
        return -1
    
    rows = len(grid)
    cols = len(grid[0])
    
    queue = deque()
    fresh = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
                
    print(f"🍊 Naranjas podridas iniciales: {list(queue)}")
    print(f"🟠 Total de naranjas frescas: {fresh}")
                
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    time = 0
    
    while queue:
        r, c, t = queue.popleft()
        time = max(time, t)
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, t + 1))
    
    return time if fresh == 0 else -1
    
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

resultado = orangesRotting(grid)
print(f"⏱️ Minutos necesarios para pudrir todo: {resultado}")
                
        
         
            
    
    




