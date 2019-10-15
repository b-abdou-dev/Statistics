# find number of pairs in given list


arr = [10, 20, 20, 10, 10, 30, 50, 10, 20, 20, 20]
n = len(arr)
count = 0
track = []
count_list = []

for i in range(n):
    for j in range(i, n):
        if arr[j] not in track:
            if arr[i] == arr[j]:
                count += 1
            else:
                continue
    count_list.append(count)
    count = 0
    track.append(arr[i])
# print(count_list)
# print(track)
result = 0
for k in count_list:
    result += k//2
print(result)