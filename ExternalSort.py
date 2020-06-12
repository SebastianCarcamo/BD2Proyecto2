import pandas as pd
import sys
import os
import json
from TweetContainer import * 
from tf_idf import *


class Handler(object):
	def __init__(self,maxSize):
		self.maxSize = maxSize
		self.names = []
		for i in os.listdir("./clean/"):
			if i.endswith('.json'):
				names.append("./clean/" + i)


	def fileSize(string):
		return os.stat(string).st_size

	def jsonToCsv(output_filename):
		for i in names:
			with open(i, encoding = 'utf-8') as reader:
				df = pd.read_json(reader)

			df.to_csv(output_filename,encoding='utf-8', index = False, header = False, mode = 'a')

	def processChunks(filename):
	chunks = pd.read_csv(filename, chunksize = 10, names = ["tweetId","date","text","user_id","user_name","location","retweeted","RT_text","RT_user_id","RT_user_name"], header = None)

	obj_list = []
	cnt = 1
	for chunk in chunks:
		for elem in chunk.values:
			obj_list.append(TweetContainer(elem))
		chunkName = 'chunk' + str(cnt) + 'tf_df' + '.csv'
		print(generate_tf_fd(obj_list))
		cnt+=1
