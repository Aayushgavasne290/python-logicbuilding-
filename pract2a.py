# create a hertorogenous list of numbers and names .split the list from highest number 
n = [12, 34, 56, 78, 90, "John", "Alice", "Bob", "Eve"]
numbers = [x for x in n if isinstance(x, int)]
names = [x for x in n if isinstance(x, str)]
print("Numbers:", numbers)
print("Names:", names)
