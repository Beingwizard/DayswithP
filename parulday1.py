#This is simple way
# row=int(input('Enter the number of row: '))
# column=int(input('Enter the number of column: '))
# pattern = "*"
# for i in range(row):
#     print(pattern * column)

#Another way of printing the pattern
# row=int(input('Enter the number of row: '))
# column=int(input('Enter the number of column: '))
# for i in range(row):
#     for j in range(column):
#         print("X", end = " ")
#     print(" ")
#Printing multi-star pattern
# num_rows = int(input("Enter the number of rows: "))
# for i in range(1, num_rows + 1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
#another pattern
# num_rows = int(input("Enter the number of rows: "))
# for i in range(1, num_rows + 1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()
#Another Pattern
# num_rows = int(input("Enter the number of rows: "))
# for i in range(1, num_rows + 1):
#     print((str(i)+ " ") * i)
# #Another Pattern
# num_rows = int(input("Enter the number of rows: "))
# for i in range(1,num_rows + 1):
#     for j in range(i):
#         print(i, end=" ")
#     print()
#Another Pattern
# num_rows = int(input("Enter the number of rows: "))
# for i in range(num_rows, 0, - 1):
#     for j in range(i):
#         print('X', end=" ")
#     print()
#Another Pattern
# num_rows = int(input("Enter the number of rows: "))
# for i in range(num_rows, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()
#Advance patterns
# N= int(input())
# for i in range(1, N + 1):
#     spaces = " " * (N - i)
#     asterisks = "*" * (2 * i - 1)
#     print(spaces + asterisks + spaces)

# N = int(input())
# for i in range(1, N + 1):
#     for j in range(N - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()