n,m = map(int,input().split())

x,y,direction = map(int,input().split())

matrix = []
d = []

for i in range(n):
    d.append([0]*m)

#지도 인풋받기
for i in range(n):
    matrix.append(list(map(int, input().split())))
    
#현재위치    
d[x][y] = 1

def turnleft():
    global direction
    direction -= 1
    if direction ==-1:
        direction = 3
        
dx =[-1,0,1,0]
dy= [0,1,0,-1]

count = 1
turn_time = 0

while True:
    
    turnleft()
    
    nx = x + dx[direction] 
    ny = y + dy[direction]
    
    if matrix[nx][ny] == 0 and d[nx][ny] == 0:
        d[nx][ny] = 1
        count += 1
        x,y = nx,ny
        turn_time = 0
    
    else:
        turn_time += 1
        
    if turn_time == 4:
        nx = x - dx[direction] 
        ny = y - dy[direction] 
        
        if matrix[nx][ny] == 1:
            break
        
        x,y = nx,ny
        turn_time = 0
    
    
print(count)
    
    
    
    
    
            