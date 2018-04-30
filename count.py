
# coding: utf-8

# In[105]:


import re
words = re.findall(r'\w+', open('Data.txt').read().lower())
Counter(words).most_common()

