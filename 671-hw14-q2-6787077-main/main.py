# YOUR CODE HERE
text = input()
words = text.split()

count = {}
for word in words:
    duplicated_words = ''.join(char for char in word if char.isalnum())
    if duplicated_words:
        count[duplicated_words] = count.get(duplicated_words, 0) + 1

dup = {word: count for word, count in count.items() if count > 1}

if dup:
    for word, count in dup.items():
        print(f"{word}: {count}")
else:
    print("no duplicated word")
