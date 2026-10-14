# print the total numbers of words

with open("data.txt", "r" ) as file:
    content = file.read()

words = content.split()
print("TOTAL WORDS:", len(words))

uniue_words = list(set(words))
print("unique words", uniue_words)