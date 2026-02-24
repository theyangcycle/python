a = int(input())
for b in range(a):
    r,w,h = list(map(float,input().split()))
    result = []
    for i in range(int(w)+1):
        for j in range(int(h)+1):
            if i**2+j**2 > r**2:
                result.append([i,j])
    for i,j in result:
        print(f"{i},{j}")