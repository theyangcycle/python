a = int(input())
for b in range(a):
    R,C = list(map(int,input().split(',')))
    r1,c1 = list(map(int,input().split(',')))
    r2,c2 = list(map(int,input().split(',')))
    if (r1+c1)%2 == (r2+c2)%2:
        print('Yes')
    else:
        print('No')