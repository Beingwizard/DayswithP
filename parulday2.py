# import array as arr
# a = arr.array('i', [1,2,3])
# print("This is the newly created array!", end = ' ')
# for i in a:
#     print(i, end = ' ')
# print("what's this?")
#Finding the largest element in the array using max function
# n = int(input("Input the size of array here: "))
# arr= []
# for i in range(n):
#     element=int(input(f"Enter element {i +1}: "))
#     arr.append(element)
# largest_element = max(arr)
# print(f"The largest element in the array is {largest_element} and all set!!")

# #Biwi ne dath dia yha max nhi use krna........
# n = int(input("Input the size of array here: "))
# arr= []
# for i in range(n):
#     element=int(input(f"Enter element {i +1}: "))
#     arr.append(element)
# max_element = arr[0]
# for element in arr:
#     if element > max_element:
#         max_element = element
# print("The largest element is: ", max_element)

# #Finding the 2nd largest element in the array
# second_max = float('-inf')
# for element in arr:
#     if element != max_element and element > second_max:
#         second_max = element
# if second_max == float('-inf'):
#     print("there is no second largest number.")
# else:
#     print("The second largest element is:", second_max)

n = 5
a = [1, 2, 3, 4, 5]
is_sorted = all(a[i] <= a[i+1] for i in range(len(a)-1))
if is_sorted:
    print(1)
else:
    print(0)