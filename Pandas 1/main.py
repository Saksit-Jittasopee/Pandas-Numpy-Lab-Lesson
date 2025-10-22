# YOUR CODE HERE
import pandas as pd

path = 'data.csv'
data = pd.read_csv(path)
data.head()

def count_word(word):
    return data['text'].str.count(word).sum()

word_search = input()
count = count_word(word_search)
print(count)
