a = int(input())
for b in range(a):
    speed, dist = list(map(float,input().split(':')))
    if speed == 0:
        print("SAFE")
    else:
        time = dist/speed
        if time <= 1:
            print("SWERVE")
        elif time <= 5:
            print("BRAKE")
        else:
            print("SAFE")