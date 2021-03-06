# Project 2 - Data Bases II

In this project we will build a secondary memory index for tweets, and build a search engine for term search, for similar tweets retrieval.

## Tweet Processing

We first process each Tweet independently in order to tokenize and remove stop words and miscellaneous character as punctuation signs and emojis. From here, each term is ready to generate the document frequency.


## TFIDF Scoring

We calculate the IDF for documents along with their TF. This is done along the splitting of chunks and is concatenated with each of them. Finally, with the master data, we can make queries. When a query is passed it is interpreted as a document and the corresponding TF-IDF is calculated for each word. Then we find the documents for which this words are not 0. That means, there will be a comparison bigger than 0, and calculate the TF_IDF of the data vectors. Finally we calculate the cosine similarity for the vector in the query and the vector in each of the to be evaluated documents and sort them.


## Web Browser

In order to build a web application for our search engine we used Django Web Framework. As this is a Python framework,it is completely compatible with our Python index. In order to search we just created an API endpoint to call the function that retrieves the similar tweets.

## Secondary Memory Management

We are given a directory full of .json files where each file corresponds to a number of tweets with their respective data. For ease of implementation, we merged all those files into a single "tweets.csv" with the function jsonToCsv() where we will be reading all the information from from now on.

Since we can't read all the tweets at once because of memory restrictions, we will be reading in chunks of size 1000 and running the generate_tf_fd() function for each chunk and writing the resulting dataframe (sorted by word) to disk.

Now that we have all the tables written in disk, we need to merge said tables into a single one so we have all the info in one file. The same problem as before arises, we can't read all the chunks into memory to merge then and make them into one, so what we do here is read the first n entries from every chunk in disk merge those and write that in the "merged.csv" file. When run that function until we have read all the lines in the written chunks. The result is a sorted file where all the tables have been merged.

