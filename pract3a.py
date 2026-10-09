# aaccept the name check if its palindrome or not
name = input("Enter the name: ")
another_name = name.lower()
if another_name == another_name[::-1]:
    print("its a palindrome")
else:
    print("its not a palindrome")