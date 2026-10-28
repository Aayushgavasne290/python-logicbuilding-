# #  file operations 
# def my_func(animal,name):
#     print("i have a ",animal)
#     print("my name is ",name)
# my_func(name="aayush",animal="dog")    

# with open("file.txt","w") as f:
#     f.write("new file created\n")

# with open("file.txt","a") as f:
#     f.write("newly added contents in div a")

# with open("file.txt","r") as f:
#     for i in f:
#         print(i)

# def greeting(name):
#     def hello():
#         return "hello " + name +"!"
#     return hello
# greet= greeting("students")

# print(greet())

# students = ["aditi","rahul"]
# students.append("karan")
# print(students)
# # student_info = (101,"aditi","mca01")

# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1
        
# for num in count_up_to(10):
#     print(num)        
# def isPalindrome(self, x: int) -> bool:
#     original = x
#     reverse = 0
#     if x < 0:
#         return False
#     while x > 0:
#         digit = x % 10
#         reverse = reverse * 10 + digit
#         x //= 10  # <--- HERE!
#     return original == reverse
# sol = isPalindrome()
# print(isPalindrome(121))

# num = int(input("enter no"))
# sum=0
# n=num
# while(n>0):
#     d=n%10
#     sum=sum*10+d
#     n=n//10
    
# if(sum==num):
#     print("the no is palirdome")
# else:
#     print("the no is not palirdome")        


# NOW PRIME AND NOT PRIME:

# num = int(input("enter a no:"))
# flag = 0
# for i in range(2,(num//2)+1):
#     if(num%i)==0:
#         flag=1
#         break
#     if(flag==0):
#      print("")    
     
#      # even odd 
     
#      def my_decorator(func):
#          def wrapper():

def sum_of_array(n,arr):
    total = 0
    for num in arr:
        total += num
    return total    
my_number = [1,2,3,4,5]
length_of_list = 5
print((my_number,length_of_list))