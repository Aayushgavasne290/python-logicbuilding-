def lcm(n1, n2):
    i = max(n1, n2)

    while True:
        if i % n1 == 0 and i % n2 == 0:
            return i
        i += 1