
# coding: utf-8

# In[ ]:


import sys
d = open("Data.txt", "r")
wordcount={}
for word in d.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
       wordcount[word] += 1

f = open('Results.txt', 'w')
sys.stdout = f

for k,v, in sorted(wordcount.items(), key=lambda words: words[1], reverse = True):
    print(k,v)
f.close()    

