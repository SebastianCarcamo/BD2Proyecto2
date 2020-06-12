import pandas as pd
import sys
import os
import json
import csv
from TweetContainer import * 
from tf_idf import *


class Handler(object):
	def __init__(self):
		self.names = []
		for i in os.listdir("./clean/"):
			if i.endswith('.json'):
				names.append("./clean/" + i)

	def jsonToCsv():
		for i in names:
			with open(i, encoding = 'utf-8') as reader:
				df = pd.read_json(reader)

			df.to_csv("tweets.csv",encoding='utf-8', index = False, header = False, mode = 'a')

	def processChunks(filename):
		chunks = pd.read_csv("tweets.csv", chunksize = 100, names = ["tweetId","date","text","user_id","user_name","location","retweeted","RT_text","RT_user_id","RT_user_name"], header = None)

		cnt = 1
		for chunk in chunks:
			obj_list = []
			for elem in chunk.values:
				obj_list.append(TweetContainer(elem))
			chunkName = 'chunk' + str(cnt) + 'tf_df' + '.csv'
			(generate_tf_fd(obj_list).sort_values(by=['word'])).to_csv(chunkName,index = False, encoding = 'utf-8')
			cnt+=1

	def writeLine(name,lista): 
		with open(name,'a+') as f:
			write = csv.writer(f)
			write.writerow(lista)


	def mergeTables():
		class TableClass:
			def __init__(self, tableName):
				self.name = tableName
				self.sizeOfChunk = 10
				self.last = False
				self.empty = False
				self.iteration = 0
				self.orderedList = (pd.read_csv(tableName,skiprows = self.iteration, nrows = self.sizeOfChunk)).values.tolist()
				self.size = sum(1 for row in pd.read_csv(tableName))

			def getFirst(self):
				return self.orderedList[0][0]

			def __lt__(self,other):
				return (self.getFirst()) < (other.getFirst())

			def updateList(self):
				self.iteration += 1
				if(self.iteration*self.sizeOfChunk<self.size):
					skip = self.iteration*self.sizeOfChunk
				elif(self.iteration*self.sizeOfChunk == self.size):
					skip = self.iteration*self.sizeOfChunk
					self.last = True
				else:
					skip = self.size - (self.iteration-1)*self.sizeOfChunk
					self.last = True
				self.orderedList = (pd.read_csv(self.name,skiprows = skip, nrows = self.sizeOfChunk)).values.tolist()

			def popFirst(self):
				value = self.orderedList.pop(0)
				if(len(self.orderedList) == 0 and self.last == True):
					self.empty = True
				if(len(self.orderedList) == 0):
					self.updateList()
				return value

		tableClasses = []
		for i in os.listdir("../docs"):
			if i.endswith('tf_df.csv'):
				tableClasses.append(TableClass("../docs/" + i))

		heapq.heapify(tableClasses)
		while(len(tableClasses) > 0):
			writeLine("merged.csv",(tableClasses[0]).popFirst())
			if(tableClasses[0].empty == True):
				tableClasses.pop(0)
			heapq.heapify(tableClasses)