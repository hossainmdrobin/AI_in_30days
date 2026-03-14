import re
from collections import Counter
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
with open('text.txt','r') as f:
    text = f.read()
    # print(text) #pure text
print(text)
print("----------------------------------------------------------------------")

text = text.lower()

text = re.sub(r"[^\w\s]","",text)

words = text.split()

word_count = Counter(words)

common = word_count.most_common(5) #array of set {} of the word and count
print(common)

# freq = FreqDist(words)
# print(freq.most_common(), "its nltk")

words = [w[0] for w in common]
counts = [w[1] for w in common]

plt.bar(words,counts)
plt.xlabel("The works")
plt.ylabel('Frequency')
plt.title('Eord frequency')
plt.show()
