# read all lines from the file ino the list ,print the total number s of lines and display the 2  and  4 line
file = open("data.txt","r")
lines = file.readlines()

print("total lines:", len(lines))

print("second line", lines [1].strip())
print("fourth line", lines [3].strip())

file.close()