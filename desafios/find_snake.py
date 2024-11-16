def find_snake_positions(grid):
    rows = len(grid)
    cols = max(len(row) for row in grid)
    # Normalize grid to have the same number of columns
    grid = [row.ljust(cols) for row in grid]

    # Find the starting position 'h'
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "h":
                start_x, start_y = x, y
                break
        else:
            continue
        break
    else:
        return []  # 'h' not found

    positions = []
    positions.append([start_y, start_x])

    delta_to_arrow = {
        (1, 0): "v",
        (-1, 0): "^",
        (0, 1): ">",
        (0, -1): "<",
    }

    x, y = start_x, start_y

    while True:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny):
                delta = (x - nx, y - ny)
                required_arrow = delta_to_arrow.get(delta)
                if required_arrow and grid[nx][ny] == required_arrow:
                    positions.append([ny, nx])
                    # visited.add((ny, nx))
                    x, y = nx, ny
                    break
        else:
            break  # No more arrows pointing to current position

    print(positions)
    return positions


grid1 = [" >>h   ", " ^   v ", " ^<<<< "]

grid2 = [
    "   ",
    " h ",
    "   ",
]

grid3 = [
    "   ",
    " h<",
    "   ",
]

grid4 = [
    ">>v",
    "^h<",
    "^<<",
]

find_snake_positions(grid1)
find_snake_positions(grid2)
find_snake_positions(grid3)
find_snake_positions(grid4)
