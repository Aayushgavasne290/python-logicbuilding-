# multiplication table
# print table  of odd number from 1 to 10
for i in range(1, 10, 2):
    print(f"Multiplication table of {i}:")
    for j in range(1, 11):
        print(f"{i*j}", end="\t")
    print()