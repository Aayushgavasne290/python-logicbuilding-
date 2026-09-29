# # Sum of Digits
# num = int(input("Enter the number: "))
# sum_of_digits = 0
# while num > 0:
#     sum_of_digits += num % 10
#     num //= 10
# print("Sum of digits is:", sum_of_digits)


num = int(input("Enter the number: "))
sumnum = int(input("Enter the number: "))
sum_of_digits = 0
while num > 0:
    sum_of_digits += num % 10
    num //= 10