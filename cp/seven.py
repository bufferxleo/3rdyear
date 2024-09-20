def minMinutes(grid):
    rows, cols = len(grid), len(grid[0])
    fresh_oranges = 0
    minutes = 0

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    while True:
        new_rotten = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if is_valid(nx, ny) and grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            new_rotten.append((nx, ny))

        if not new_rotten:
            break

        minutes += 1

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                return -1

    return minutes

# Example usage:
grid = [
    [1, 1, 2],
    [1, 1, 1],
    [1, 1, 1]
]

result = minMinutes(grid)
print(result)