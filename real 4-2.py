n = input()

y = int(ord(n[0]))-int(ord('a'))+1
x = int(n[1])
count = 0


move_types = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

for i in range(8):
    
    nx = x + move_types[i][0]
    ny = y + move_types[i][1]
    
    if nx <1 or ny<1 or nx>8 or ny >8:
        continue
    
    count +=1
    
print(count)