n = int(input())
nums = list(map(int,input().split()))
counts = [1]
id = 0
while id < len(nums)-1:
    count = 0
    for j in range(id,n):
        try:
            if nums[j] <= nums[j+1]:
                count += 1
            else:
                break
        except:
            break
    id = j+1
    counts.append(count+1)
print(max(counts))