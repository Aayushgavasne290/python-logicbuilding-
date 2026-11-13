# a = 'aayush'
# b = 'ayush'
# if a ==b:
#     print("Both strings are equal")
# else:
#     print("Both strings are not equal")    
# print(a[0:3])  # Output: 'aay'

# def revstring(n):
#     if len(n)==0:
#         return n
#     else:
#         return n[-1] + revstring(n[:-1])
# result = revstring("ayush")
# print(result)  # Output: 'hsuya'    

def revstring(n):
    if len(n) == 0:
        return n
    else:
        # Take the last character and recurse with everything EXCEPT the last character? 
        # Wait, if you use n[:-1], your base logic needs to slice properly:
        return n[-1] + revstring(n[:-1])