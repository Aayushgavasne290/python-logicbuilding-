# def fibonacci(n):
#     a , b = 0 ,1
#     for _ in range(n):
#         yield a
#         a , b = b , a + b
# print(list(fibonacci(10)))        

def revstring(n):
    if len(n) == 0:
        return n
    else:
        # Take the last character and recurse with everything EXCEPT the last character? 
        # Wait, if you use n[:-1], your base logic needs to slice properly:
        return n[-1] + revstring(n[:-1])
print(revstring("ayush"))  # Output: 'hsuya'    