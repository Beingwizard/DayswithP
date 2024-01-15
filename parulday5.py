# #//merge sort without function
# def mergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         left = arr[:mid]
#         right = arr[mid:]
#         mergeSort(left)
#         mergeSort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] > right[j]:
#                 arr[k]=right[j]
#                 j+=1
#             else:
#                 arr[k]=left[i]
#                 i+=1
#             k+=1
#         while i < len(left):
#             arr[k]=left[i]
#             i+=1
#             k+=1
#         while j < len(right):
#             arr[k]=right[j]
#             j+=1
#             k+=1
# arr = [10, 7, 8, 9, 1, 5]
# mergeSort(arr)
# print(arr)


#remove duplicates from sorted array
def removeDuplicates(arr):
    if len(arr)==0 or len(arr)==1:
        return len(arr)
    j=0
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            arr[j]=arr[i]
            j+=1
    arr[j]=arr[len(arr)-1]
    j+=1
    return j
arr = [1,2,2,3,4,4,4,5,5]
n = removeDuplicates(arr)
print(n)
for i in range(n):
    print(arr[i],end=" ")


