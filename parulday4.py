#binary sort
# sorted_arr = [int(x) for x in input("Enter a soted array with space: ").split()]
# target = int(input("Enter the target element"))
# low = 0
# high = len(sorted_arr)-1

# found = False

# while low<=high:
#     mid = (high-low)//2 + low #Parul: This is the correct way to calculate mid

#     if sorted_arr[mid] == target:
#         print(f'Target {target} found at index {mid}.')
#         found = True
#         break
#     elif sorted_arr[mid] > target:
#         high = mid -1
#     else:
#         low = mid +1
# if not found:
#     print(f'Target {target} not found in the list.')


# bubble sort without function and using for loop
arr = [int(x) for x in input("Enter a array with space: ").split()]
print(arr)
for i in range(len(arr)):
    for j in range(len(arr)-1):
    if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

#selection sort without function and using for loop
arr = [int(x) for x in input("Enter a array with space: ").split()]
print(arr)
for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)

#insertion sort without function and using for loop
arr = [int(x) for x in input("Enter a array with space: ").split()]
print(arr)
for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j>=0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
    print(arr)
    