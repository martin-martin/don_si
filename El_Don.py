##############################################################################
######### Analyzing a free-form literary Corpus for word frequencies #########
##############################################################################
import re
# requires Python 3.x
from pathlib import Path
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


########################### Pt.1 - Getting the data ###########################

stop_words = set(stopwords.words("Spanish"))
# import literature
# Thanks Project Gutenberg: http://www.gutenberg.org/cache/epub/2000/pg2000.txt
file_path = "cervantes_quijote.txt"
text = Path(file_path).read_text()


####################### Pt.2 - Getting the data in shape ######################

# First I will separate the companion info text from the actual novel.
# this final intro word is gleaned from checking out the text string
text_info_end = "Abela."
info_end_index = text.find(text_info_end)
info_end = info_end_index + len(text_info_end)
# creating a variable holding the text info
text_info = text[: info_end]
# and another one with the Spanish novel
dq_start = text.find("El ingenioso hidalgo")
don_quijote = text[dq_start:]

# I'll remove newlines while keeping "sentence" information.
# For this I will treat headings as "sentences"
# and as separate pieces of meaning.

# this regex pipe replaces all occurances of at least 2 consecutive newlines
# with a dot followed by a whitespace
# if the line before the first newline character ends with a letter
# (not a sentence delimiter)
regex =  re.compile(r"(?<=\w)\n{2,}")
don_quijote = re.sub(regex, ". ", don_quijote)
# Now I'll also remove the remaining newlines,
# replacing them simply with whitespaces.
don_quijote = don_quijote.replace("\n", " ")


############## Pt.3 - Splitting the data in pieces (tokenization) #############

# Since for this exercise I am treating the novel as a Spanish corpus,
# I now go to tokenize the text.
# looking for word frequencies, I'll need the words tokenized
dq_word_tokenized = nltk.word_tokenize(don_quijote)


##################### Pt.4 - Getting the word frequencies #####################

# source: http://www.nltk.org/book/ch01.html
# The NLTK book provides a useful library for calculating word frequencies.
from nltk.book import FreqDist
# removing stopwords and translating all words to lowercase
dq_real_words = [w.lower() for w in dq_word_tokenized if not w in stop_words]
# removing punctuation
dq_words = [w for w in dq_real_words if w.isalpha()]
fdist = FreqDist(dq_words)
print(fdist.most_common(20))


# And that's it. With inspecting the corpus and a bit of data wrangling
# here are the 20 most frequent words of Cervantes' Don Quijote.