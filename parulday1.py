# #This is simple way
# # row=int(input('Enter the number of row: '))
# # column=int(input('Enter the number of column: '))
# # pattern = "*"
# # for i in range(row):
# #     print(pattern * column)

# #Another way of printing the pattern
# # row=int(input('Enter the number of row: '))
# # column=int(input('Enter the number of column: '))
# # for i in range(row):
# #     for j in range(column):
# #         print("X", end = " ")
# #     print(" ")
# #Printing multi-star pattern
# # num_rows = int(input("Enter the number of rows: "))
# # for i in range(1, num_rows + 1):
# #     for j in range(i):
# #         print("*", end=" ")
# #     print()
# #another pattern
# # num_rows = int(input("Enter the number of rows: "))
# # for i in range(1, num_rows + 1):
# #     for j in range(1,i+1):
# #         print(j, end=" ")
# #     print()
# #Another Pattern
# # num_rows = int(input("Enter the number of rows: "))
# # for i in range(1, num_rows + 1):
# #     print((str(i)+ " ") * i)
# # #Another Pattern
# # num_rows = int(input("Enter the number of rows: "))
# # for i in range(1,num_rows + 1):
# #     for j in range(i):
# #         print(i, end=" ")
# #     print()
# #Another Pattern
# # num_rows = int(input("Enter the number of rows: "))
# # for i in range(num_rows, 0, - 1):
# #     for j in range(i):
# #         print('X', end=" ")
# #     print()
# #Another Pattern
# # num_rows = int(input("Enter the number of rows: "))
# # for i in range(num_rows, 0, -1):
# #     for j in range(1, i+1):
# #         print(j, end=" ")
# #     print()
# #Advance patterns
# # N= int(input())
# # for i in range(1, N + 1):
# #     spaces = " " * (N - i)
# #     asterisks = "*" * (2 * i - 1)
# #     print(spaces + asterisks + spaces)

# # N = int(input())
# # for i in range(1, N + 1):
# #     for j in range(N - i):
# #         print(" ", end="")
# #     for j in range(2 * i - 1):
# #         print("*", end="")
# #     print()
# #Counting the numbers
# # Number = int(input("Enter the num: "))
# # count = 0
# # while Number > 0:
# #     Number //= 10  
# #     count += 1     
# # print(count)
# #Pallindrome number
# # input_num = int(input("Enter a num: "))
# # num_str = str(input_num)
# # if num_str == num_str[::-1]:
# #     print(f"{input_num} is a palindrome")
# # else:
# #     print(f"{input_num} is not a palindrome")
# n = int(input("Enter the number of terms: "))
# a, b = 0, 1
# count = 0
# if n <= 0:
#     print("positive integer krde bc")
# elif n == 1:
#     print("Fibonacci sequence kidr tk?", n, ":")
#     print(a)
# else:
#     print("Fibonacci sequence h ye:")
#     while count < n:
#         print(a, end=' ')
#         temp = a + b
#         a = b
#         b = temp
#         count += 1

# n = int(input("Enter the num: "))
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=' ')
#     a, b = b, a + b
#print the 
row = int(input())
for i in range(1,row+1):
    for j in range(i):
        print(i, end= ' ')
    print(" ")