import pandas as pd
import numpy as np
import pickle

def get_relevant_words_data(file_name, tf_df):
    document_data = {}
    with open(filname, "rb") as data:
        while True:
            try:
                current_row = pickle.load(data)
                word_name = list(current_row.keys())[0] 
                if word_name in tf_df["words"].values:
                    document_data[word_name] = current_row[word_name]
            except EOFError:
                break
    return document_data

def doc_freq_to_df(d_dict):
    df = pd.DataFrame(columns = ["word", "doc_freq"]
    for key in list(d_dict.keys()):
        data_dict = {}
        data_dict["word"] = key
        data_dict["doc_freq"] = len(d_dict[key])
        new_row_df = pd.DataFrame(data_dict, index = [0])
        df = df.append(data_dict, ignore_index = True) 
    return df


def get_relevant_columns(data_dict):
    column_set = {}
    for key in list(data_dict.keys()):
        for tuples in data_dict[key]: 
            column_set.add(tuples[0])
    return list(column_set)

def get_n_most_similar(text, n):
    data_similarity = {}
    word_data = get_relevant_words_data(data_file_name, tf_df)

    freq_df = gen_term_freq(text.split(""))
    doc_freq_df = doc_freq_to_df(word_data)
    relevant_columns = get_relevant_columns(word_data)
    selected_df = df[selection_mask]

    full_df = pd.concat(freq_df, doc_freq_df)

    freq_df["tf_idf"] = freq_df.apply(lambda x: calc_tf(x["freq"]) * calc_idf(TWEET_n, x["doc_freq"]), axis=1)
    query_series = freq_df["tf_idf"]

    for col_name, series, df.iteritems():
       data_similarity[col_name] = cos_similarity(series.to_numpy), query_series.to_numpy)

    return sorted(data_similarity)[:n]
      
