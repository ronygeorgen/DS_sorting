arr = [12,3,5,1,23,4]
n = len(arr)
flag = 0
for i in range(n-1):
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            flag = 1
    if flag ==0:
        break
print(arr)