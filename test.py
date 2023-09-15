
arr = [17,18,5,4,6,1]
last = -1
for i in range(len(arr)- 1, -1, -1):
    temp = arr[i]
    arr[i] = last
    last = max(temp, last)
print(arr)