import pandas as pd
import numpy as np

def gen_doc_freq(obj_arr):
    column_names = ["word", "doc_freq"]

    df = pd.DataFrame(columns = column_names)

    for obj in obj_arr: 
        current_index = obj.id 
        for word in set(obj.wordList):
            word_series = df[df["word"] == word]
            if word_series.empty:
                data_dict = {}
                data_dict["word"] = word
                data_dict["doc_freq"] = 1
                new_row_df = pd.DataFrame(data_dict, index = [0])
                df = df.append(data_dict, ignore_index = True)
            else:
                df.loc[df["word"] == word, "doc_freq"] += 1
    return df

def gen_term_freq(word_array):
    df = pd.DataFrame(columns = ["word", "freq"])
    for w in set(word_array): 
        tf_w = word_array.count(w)
        data_dict = {}
        data_dict["word"] = w
        data_dict["freq"] = tf_w
    return df
            
    

def generate_tf_fd(obj_arr):
    # General empy word -> tf_idf matrix
    column_names = ["word"] + [str(o.id) for o in obj_arr]
    df = pd.DataFrame(0, index = np.arange(len(obj_arr)), columns = column_names)

    # Get document frequency matrix
    freq_df = gen_doc_freq(obj_arr)

    # Iterate over each doc and assign values
    for obj in obj_arr: 
        current_index = str(obj.id)
        term_freq_df = gen_term_freq(obj.wordList)

        for word in term_freq_df["word"]:
            tf = calc_tf(term_freq_df[term_freq_df["word"] == word, "freq"])
            data_dict["word"][current_index] = tf
            data_dict["word"]["doc_freq"] = freq_df[freq_df["word"] == word, "doc_freq"]
    return df

def generate_tf_idf(obj_arr):
    # General empy word -> tf_idf matrix
    column_names = ["word"] + [str(o.id) for o in obj_arr]
    df = pd.DataFrame(0, index = np.arange(len(obj_arr)), columns = column_names)

    # Get document frequency matrix
    freq_df = gen_doc_freq(obj_arr)

    # Iterate over each doc and assign values
    for obj in obj_arr: 
        current_index = str(obj.id)
        term_freq_df = gen_term_freq(obj.wordList)

        for word in term_freq_df["word"]:
            tf = calc_tf(term_freq_df[term_freq_df["word"] == word, "freq"])
            idf = calc_idf(len(obj_arr) , freq_df[freq_df["word"] == word, "doc_freq"])
            tf_idf =  tf * idf
            data_dict["word"][current_index] = tf_idf
    return df

def calc_tf(freq):
    if freq <= 0:
        return 0
    else:
        return 1 + np.log10(freq)

def calc_idf(freq, n):
    return np.log10(n/freq)

def writeDFtoDisk(DF, name):
    DF.to_csv(name ,index = False)