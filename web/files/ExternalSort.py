import pandas as pd
import sys
import os
import json
import csv
import heapq
import ast

from files.TweetContainer import TweetContainer
from files.utils import *
from files.tf_idf import *

PATH = './store/'

class Handler:
	def __init__(self):
		self.names = []
		for i in os.listdir("./clean/"):
			if i.endswith('.json'):
				self.names.append("./clean/" + i)

	def jsonToCsv(self):
		for i in self.names:
			with open(i, encoding = 'utf-8') as reader:
				df = pd.read_json(reader)

			df.to_csv(PATH + "tweets.csv",encoding='utf-8', index = False, header = False, mode = 'a')

	def processChunks(self):
		chunks = pd.read_csv(PATH + "tweets.csv", chunksize = CHUNK_SIZE, names = ["tweetId","date","text","user_id","user_name","location","retweeted","RT_text","RT_user_id","RT_user_name"], header = None)

		for cnt, chunk in enumerate(chunks):
			obj_list = []
			for elem in chunk.values:
				obj_list.append(TweetContainer(elem))
			chunkName = 'chunks/' + str(cnt) + 'tf_df' + '.csv'
			(generate_tf_fd(obj_list).sort_values(by=['word'])).to_csv(PATH + chunkName,index = False, encoding = 'utf-8')

	def writeLine(self, name, lista): 
		with open(name,'a+') as f:
			write = csv.writer(f)
			write.writerow(lista)


	def mergeTables(self):
		class TableClass:
			def __init__(self, tableName):
				self.name = tableName
				self.sizeOfChunk = SORTED_CHUNK
				self.last = False
				self.empty = False
				self.iteration = 0
				self.orderedList = (pd.read_csv(tableName,skiprows = self.iteration, nrows = self.sizeOfChunk)).values.tolist()
				self.size = len(pd.read_csv(tableName))

			def getFirst(self):
				return self.orderedList[0][0]

			def __lt__(self,other):
				return str(self.getFirst()) < str(other.getFirst())

			def updateList(self):
				self.iteration += 1
				if((self.iteration+1)*self.sizeOfChunk-1 >= self.size):
					self.last = True
				skip = self.iteration * self.sizeOfChunk
				self.orderedList = (pd.read_csv(self.name,skiprows = skip, nrows = self.sizeOfChunk)).values.tolist()

			def popFirst(self):
				value = self.orderedList.pop(0)
				if(len(self.orderedList) == 0 and self.last == True):
					self.empty = True
				elif(len(self.orderedList) == 0):
					self.updateList()
				return value

		tableClasses = []
		for i in os.listdir(PATH + 'chunks'):
			if i.endswith('tf_df.csv'):
				tableClasses.append(TableClass(PATH + 'chunks/'+ i))
		
		heapq.heapify(tableClasses)
		while(len(tableClasses) > 0):
			tmp = []
			tmp = tableClasses[0].popFirst()
			tmp[1] = ast.literal_eval(tmp[1])
			while(tableClasses[0].empty == True):
				tableClasses.pop(0)
			heapq.heapify(tableClasses)
			while(tableClasses[0].getFirst() == tmp[0]):
				tmp[1].update(ast.literal_eval(tableClasses[0].popFirst()[1]))
				while(tableClasses[0].empty == True):
					tableClasses.pop(0)
				heapq.heapify(tableClasses)
			self.writeLine(PATH + "merged.csv",tmp)
			heapq.heapify(tableClasses)
