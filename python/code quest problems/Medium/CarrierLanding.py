t = int(input())
for _ in range(t):
    a = int(input())
    for b in range(a):
        name = input()
        airx,airy = map(float,input().split(','))
        startx,starty = map(float,input().split(','))
        endx,endy = map(float,input().split(','))
        slopes = [(starty-airy)/(startx-airx),(endy-airy)/(endx-airx)]
        if -1.6<=slopes[0]<=-0.8 and -1.6<=slopes[1]<=-0.8:
            print(f'{name}, Clear To Land!')
        else:
            print(f'{name}, Abort Landing!')