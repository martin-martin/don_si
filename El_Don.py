
# coding: utf-8

# # Analyzing a free-form literary Corpus for word frequencies

# ## Pt.1 - Getting the data

# In[98]:

import re
from pathlib import Path
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


# In[99]:

stop_words = set(stopwords.words("Spanish"))


# In[100]:

# import literature
# Thanks Project Gutenberg: http://www.gutenberg.org/cache/epub/2000/pg2000.txt
file_path = "cervantes_quijote.txt"
text = Path(file_path).read_text()


# In[101]:

#print(text[:1000])


# ## Pt.2 - Getting the data in shape

# First I will separate the companion info text from the actual novel.

# In[102]:

# this final intro word is gleaned from checking out the text string
text_info_end = "Abela."
info_end_index = text.find(text_info_end)
info_end = info_end_index + len(text_info_end)
# creating a variable holding the text info
text_info = text[: info_end]
# and another one with the Spanish novel
dq_start = text.find("El ingenioso hidalgo")
don_quijote = text[dq_start:]


# In[103]:

print(don_quijote[:500])


# I'll remove newlines while keeping "sentence" information. For this I will treat headings as "sentences" and as separate pieces of meaning.

# In[104]:

# this regex pipe replaces all occurances of at least 2 consecutive newlines
# with a dot followed by a whitespace
# if the line before the first newline character ends with a letter (not a sentence delimiter)
regex =  re.compile(r"(?<=\w)\n{2,}")
don_quijote = re.sub(regex, ". ", don_quijote)
print(don_quijote[:500])


# Looking good. Now I'll also remove the remaining newlines, replacing them simply with whitespaces.

# In[105]:

don_quijote = don_quijote.replace("\n", " ")
don_quijote[:500]


# ## Pt.3 - Splitting the data in pieces (tokenization)

# Since for this exercise I am treating the novel as a **Spanish corpus**, I now go to tokenize the text.

# In[106]:

dq_sent_tokenized = nltk.sent_tokenize(don_quijote)
# I won't be using the tokenized sentences here, but let's see how many there are
print(len(dq_sent_tokenized))


# In[107]:

# looking for word frequencies, I'll need the words tokenized
dq_word_tokenized = nltk.word_tokenize(don_quijote)


# ## Pt.4 - Getting the word frequencies

# [The NLTK book](http://www.nltk.org/book/ch01.html) provides a useful library for calculating word frequencies.

# In[108]:

from nltk.book import FreqDist
fdist = FreqDist(dq_word_tokenized)


# In[109]:

print(fdist)


# In[110]:

fdist.most_common(20)


# Okay, neat. Let's remove the stopwords and punctuation.

# In[111]:

# removing stopwords and translating all words to lowercase
dq_real_words = [w.lower() for w in dq_word_tokenized if not w in stop_words]


# In[112]:

# removing punctuation
dq_words = [w for w in dq_real_words if w.isalpha()]


# In[113]:

fdist = FreqDist(dq_words)


# In[114]:

print(fdist)


# In[115]:

fdist.most_common(20)


# And that's it. With inspecting the corpus and a bit of data wrangling here are the word frequencies of Cervantes' Don Quijote.
