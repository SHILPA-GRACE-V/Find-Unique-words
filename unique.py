text_file = open('fruit.txt', 'r')
text = text_file.read()
text = text.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]
unique = []
for word in words:
    if word not in unique:
        unique.append(word)
unique.sort()
print(unique)
