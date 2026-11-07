# def square(n):
#     """Generator function that yields the square of numbers from 0 to n-1."""
#     for i in range(n):
#         yield i * i 

# def fibonacci(n):
#     """Generator function that yields the Fibonacci sequence up to n terms."""
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
        
        # def sumof_squares(n):
            
        #     total = 0
        #     for i in range(n):
        #         total += i * i
        #         yield total
        
        
        # def sumoftwo(n):
        #     """Generator function that yields the sum of squares of two numbers from 0 to n-1."""
        #     for i in range(n):
        #         for j in range(n):
        #             yield i * i + j * j
        # print(list(sumoftwo(3)))  # Output: [0, 1, 4, 1, 2, 5, 4, 5, 8]          
        
        
        def primenum(n):
            """Generator function that yields prime numbers up to n."""
            for num in range(2, n + 1):
                is_prime = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    yield num  