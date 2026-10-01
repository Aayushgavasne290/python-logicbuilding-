# n=int(input("enter the no of rows:"))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j), end=" ")
#     print()    


# new pattern3 
# n=int(input("enter the no of rows:"))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+i), end=" ")
#     print()    


#  new pattern 4 
n=int(input("enter the no of rows:"))
num= 0
for i in range(n):
    for j in range(i+1):
        print(chr(65+num), end=" ")
        num+=1
    print()    