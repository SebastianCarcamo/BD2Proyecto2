import json
from nltk.corpus import stopwords 
from nltk.tokenize import TweetTokenizer
from nltk.stem import SnowballStemmer

punctuation = [",",".","¿","?",":","...","!","¡"]

stop_words = set(stopwords.words('spanish'))
ss = SnowballStemmer('spanish')

class TweetContainer:
	def __init__(self,tweet):
		self.id = tweet["id"]
		text = tweet["text"]
		tknzr = TweetTokenizer(preserve_case=False,strip_handles=True, reduce_len=True)
		self.tokenized = tknzr.tokenize(text)
		self.filtered = [w for w in self.tokenized if not w in stop_words and w not in punctuation and w not in ["rt"]]
		stemmed = []
		for w in self.filtered:
			stemmed.append(ss.stem(w))
		
		self.wordList = stemmed