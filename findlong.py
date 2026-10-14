# find the longest  word in a user - enter sentence
sentence = input("enter a sentence:")
words = sentence.split()

longest = max(words , key=len)

print("words:", words)
print("longest word:",longest)