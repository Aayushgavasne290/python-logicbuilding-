#def add(a,b):
 #   return a + b
#print(add(9,3))



#
#add_lambda = lambda a, b: a + b
# print(add_lambda(5,7))
#

# number_list = [1, 2, 3, 4, 5]
# def get_number_list():
#     return number_list
# print(get_number_list())

# def square_num(get_number_list):
#     return get_number_list() * get_number_list()
# print(square_num(5))




number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(number_list)
# result_set= map(lambda x: x * x, number_list)
# print(list(result_set))

# def isodd(num):
#     return num%2!=0
# result_set= map(isodd, number_list)
# print(list(result_set))


# here we have used filter function to filter even numbers with map function to square the even numbers

# result_set=map(lambda x:x*x,filter(lambda x:x%2==0,number_list))
# print(list(result_set)) 

student_list=[{"name": "Alice", "marks": [20, 30, 40]}, {"name": "Bob", "marks": [22, 32, 42]}, 
              {"name": "Charlie", "marks": [23, 33, 43]}, {"name": "David", "marks": [21, 89, 41]}, 
              {"name": "Eve", "marks": [25, 35, 45]}]

print(student_list)

avg_cal=map(lambda s:{"name": s["name"], "average": sum(s["marks"])/len(s["marks"])} ,student_list)
print(list(avg_cal))