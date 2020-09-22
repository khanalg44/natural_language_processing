#!/usr/bin/env python

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def prepare_text(text, TOKENIZE=False, STEM=False):
    text = text.lower() # lowercase text
    text = REPLACE_BY_SPACE_RE.sub(' ',text) # replace REPLACE_BY_SPACE_RE symbols by space in text
    text = BAD_SYMBOLS_RE.sub('', text)# delete symbols which are in BAD_SYMBOLS_RE from text
    text = ' '.join([word for word in text.split() if word not in STOPWORDS]) # delete stopwors from text

    if STEM:
        text = text.split()
        p_stemmer = PorterStemmer()
        text = [p_stemmer.stem(doc) for doc in text]
        return text

    if TOKENIZE: # split the text into words
        return text.split()
        # Another way to do it
        #from nltk.tokenize import RegexpTokenizer
        #tokenizer = RegexpTokenizer(r'\w+')
        #text = tokenizer.tokenize(text_)

    return text



