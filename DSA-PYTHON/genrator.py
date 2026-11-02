def square(n):
    """Generator function that yields the square of numbers from 0 to n-1."""
    for i in range(n):
        yield i * i