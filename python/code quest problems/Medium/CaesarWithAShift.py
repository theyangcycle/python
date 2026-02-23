abc = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
a = int(input())
for b in range(a):
    message = input().lower()
    shift = list(map(int,input().split()))
    direction = list(map(int,input().split()))
    output = []
    i = 0
    for v in message:
        if v in abc:
            if direction[i%len(direction)]:
                x = abc.index(v) - shift[i%len(shift)]
                output.append(abc[x])
            else:
                x = abc.index(v) + shift[i%len(shift)]
                if x > 25:
                    output.append(abc[x-26])
                else:
                    output.append(abc[x])
            i+=1
        else:
            output.append(v)
    print(''.join(output))