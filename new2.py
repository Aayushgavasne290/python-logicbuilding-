def square(n):
  for i in range(n):
       i*i
print(square)       

def square(n):
  for i in range(n):
    yield i*i
print (square)    