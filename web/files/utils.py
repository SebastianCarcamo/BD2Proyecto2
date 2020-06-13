import pandas as pd
import numpy as np
import pickle
import ast
import math

from files.TweetContainer import TweetContainer
from files.tf_idf import *
from files.constants import *
from files.calc_utils import *

PATH = "./store/"

def get_relevant_words_data(word):
	l = 0
	r = NUM_TERMS - 2

	while l <= r:
		m = (l + r) // 2
		row = pd.read_csv(PATH + 'merged.csv', skiprows = m, nrows = 1).values.tolist()
		if word == str(row[0][0]):
			return {word : [(k, v) for k, v in ast.literal_eval(row[0][1]).items()]}
		if str(row[0][0]) < word:
			l = m + 1
		else:
			r = m - 1
	return {word : []}

def doc_freq_to_df(d_dict):
	df = pd.DataFrame(columns = ["word", "doc_freq"])
	for key in list(d_dict.keys()):
		data_dict = {}
		data_dict["word"] = key
		data_dict["doc_freq"] = len(d_dict[key])
		new_row_df = pd.DataFrame(data_dict, index = [0])
		df = df.append(data_dict, ignore_index = True) 
	return df


def get_relevant_columns(data_dict):
	column_set = set()
	for key in list(data_dict.keys()):
		for tuples in data_dict[key]: 
			column_set.add(tuples[0])
	return list(column_set)

def get_n_most_similar(text, n):
	tweet = TweetContainer([0, 0, text])
	processed_text = tweet.wordList

	word_data = {}
	for word in set(processed_text):
		word_data = {**word_data, **get_relevant_words_data(word)}
		

	doc_freq = {}
	documents = {}
	for word, term_freq in word_data.items():
		doc_freq[word] = len(term_freq) + 1
		for doc, freq in term_freq:
			if doc not in documents:
				documents[doc] = {}
			documents[doc][word] = freq

	query_freq = {}
	for word in processed_text:
		if word not in query_freq:
			query_freq[word] = 0
		query_freq[word] += 1
	
	tfidf_query = {}
	query_arg = 0
	for word in set(processed_text):
		tfidf_query[word] = calc_tf(query_freq[word]) * calc_idf(doc_freq[word], DOCUMENT_COUNT)
		query_arg += tfidf_query[word]**2
	query_arg = math.sqrt(query_arg);
	
	score_id = []
	for doc, term_freq in documents.items():
		score = 0
		doc_arg = 0
		for word, freq in term_freq.items():
			tfidf = calc_tf(freq) * calc_idf(doc_freq[word], DOCUMENT_COUNT)
			score += tfidf * tfidf_query[word]
			doc_arg += tfidf**2
		doc_arg = math.sqrt(doc_arg)
		score /= doc_arg * query_arg
		score_id.append((score, doc))
	
	score_id.sort(key=lambda tup: tup[0], reverse = True) 
	print(score_id[:n])
	return score_id[:n]
