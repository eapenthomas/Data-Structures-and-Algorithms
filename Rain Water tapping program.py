# DFS on a 3x3 matrix

# 3x3 matrix (can be values or just coordinates)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows, cols = len(matrix), len(matrix[0])
visited = [[0 for _ in range(cols)] for _ in range(rows)]
for row in visited:
    for col in row:
        print(col,end=" ")
    print()

# Directions: up, down, left, right
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def dfs(r, c):
    # boundary + visited check
    if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c]:
        return

    visited[r][c] = True
    print(matrix[r][c], end=" ")  # Process the node (here: print)

    # Explore neighbors
    for dr, dc in directions:
        dfs(r + dr, c + dc)


# Start DFS from top-left (0,0)
# dfs(0, 0)
