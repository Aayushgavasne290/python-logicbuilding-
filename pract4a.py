# # sum of digits of a number
# num = int(input("enter a number: "))
# sum = 0
# total = 0
# while num > 0:
#     total += num % 10
#     num //= 10
#     # digit = num % 10
#     # sum += digi/
#     # num //= 10
# print("Sum of digits:", num)


# sum of digits of a number
num = int(input("enter a number: "))
num = abs(num)   # handle negative numbers
total = 0

while num > 0:
    total += num % 10
    num //= 10

print("Sum of digits:", total)