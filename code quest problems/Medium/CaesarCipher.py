abc = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
a = int(input())
for b in range(a):
    shift = int(input()) % 26
    string = input()
    output = []
    for i in string:
        if i == ' ':
            output.append(i)
            continue
        x = abc.index(i) - shift
        if 0 > x:
            output.append(abc[26+x])
        else:
            output.append(abc[x])
    print(''.join(output))