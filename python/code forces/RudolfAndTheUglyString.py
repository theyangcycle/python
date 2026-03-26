for b in range(int(input())):
    n = int(input())
    s = input()
    map = 0
    pie = 0
    count = 0
    for i in s:
        if i == 'map'[map]:
            map+=1
        elif i == 'm':
            map = 1
        else:
            map = 0
        
        if i == 'pie'[pie]:
            if map == 3:
                pie = 0
            else:
                pie+=1
        elif i == 'p':
            pie = 1
        else:
            pie = 0
        
        if map == 3:
            count += 1
            map = 0
        if pie == 3:
            count += 1
            pie = 0

    print(count)