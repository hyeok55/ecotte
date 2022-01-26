from collections import deque

n,m = map(int,input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int,input())))
    
    
count = 1
x,y =0,0

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

queue = deque()
queue.append((x,y))
def bfs():
    
    while queue:
        
        x,y = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny <0 or nx > n-1 or ny > m-1:
                continue
            
            if matrix[nx][ny] == 0:
                continue
            
            if matrix[nx][ny] == 1:
                
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx,ny))
                
                
                
bfs()
print(matrix[n-1][m-1])
                