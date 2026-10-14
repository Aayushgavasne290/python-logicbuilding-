# write a program to read a file and count how many vovwels are present in it
file = open("data.txt", "r")
content = file.read()
count=0
for ch in content:
    if ch.lower() in "aeiou":
        count+=1
print("total vowels",count)

file.close()