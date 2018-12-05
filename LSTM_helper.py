#!/home/ubuntu/anaconda3/bin/python

import pandas as pd
from tqdm import tqdm
df = pd.read_pickle("typeAB_not_0.pickle")

review = df['review']
y = df['stars']


import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
def sentence_tokenizer(s):
    """sentence tokenizer --modified from EDA version
    :parameter
        s: String
    :return
        tokenized_s: String"""
    s = s.lower()
    tokenized_s = nltk.word_tokenize(s)
    english_stopwords = set(stopwords.words('english'))
    tokenized_s = [w for w in tokenized_s if w not in english_stopwords if w.isalpha()]
    tokenized_s = " ".join(tokenized_s)
    return tokenized_s

X = []
for i in tqdm(range(len(review))):
    X.append(sentence_tokenizer(review[i]))

processed_df = pd.DataFrame({'review':X,'star':y})
processed_df.to_pickle('processed_typeAB_not_0.pickle')



