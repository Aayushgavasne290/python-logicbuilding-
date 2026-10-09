# to form a pyramid of numbers using for loop
# n = int(input("enter the number :")) 
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print('*', end=" ")
#     if i==1:
#         print    
#     print()

for i in range(1, 5):
    if i == 1:
        print("*" * i)
    elif i == 2:
        print("#" * i)
    elif i == 3:
        print("&" * i)
    elif i == 4:
        print("@" * i)     

