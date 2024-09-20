#7

def ans(grid):
    m=len(grid)
    n=len(grid[0])
    
    min_minutes=0
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    
    def valid(x,y):
        if 0<=x<m and 0<=y<n:
            return True
        return False
    
    
    while True:
        change=False
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    for dx,dy in directions:
                        nx=i+dx
                        ny=j+dy
                        if vaild(nx,ny) and grid[nx][ny]==1:
                            grid[nx][ny]=2
                            change=True
        if change==False:
            break
            
        min_minutes+=1
        
        for i in grid:
            for j in i:
                if j==1:
                    return -1
        return min_minutes
        



grid=[[2,1,1],[1,1,0],[0,1,1]]

print(ans(grid))
