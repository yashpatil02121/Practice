def numIslands(grid):
    if not grid:
        return 0
    
    rows = len(grid)
    columns = len(grid[0])

    islands_count = 0

    def dfs(r,c):

        # Check if r and c are out of bounds or the cell is water
        if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] == '0':
            return
        
        # Mark the current land cell as visited by changing it to '0'
        grid[r][c] = '0'

        # Call the DFS in all 4 directions
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)

    # Go through every cell in the grid
    for r in range(rows):
        for c in range(columns):
            # If it's land, it's a new island
            if grid[r][c] == '1':
                islands_count += 1
                dfs(r,c) # Sink the island

    return islands_count


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid)) 