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
        new_row_df = pd.DataFrame(data_dict, index = [0])
        df = df.append(data_dict, ignore_index = True)
    return df
            
    

def generate_tf_fd(obj_arr):
    # General empy word -> tf_idf matrix
    column_names = ["word"] + [str(o.id) for o in obj_arr]
    df = pd.DataFrame(columns = column_names)

    # Get document frequency matrix
    freq_df = gen_doc_freq(obj_arr)

    # Iterate over each doc and assign values
    for obj in obj_arr: 
        current_index = str(obj.id)
        term_freq_df = gen_term_freq(obj.wordList)
        word_series = term_freq_df["word"]

        for word in word_series:
            freq = term_freq_df[term_freq_df["word"] == word]["freq"].values
            tf = calc_tf(freq[0])
            word_freq = freq_df[freq_df["word"] == word]["doc_freq"].values[0]

            # If already in df update value for a given doc
            if word in df["word"].values:

                df.loc[df["word"] == word, current_index] = tf
                df.loc[df["word"] == word, "doc_freq"] = word_freq
                continue
            data_dict = {}
            data_dict["word"] = word
            data_dict[current_index] = tf
            data_dict["doc_freq"] = word_freq
            new_row_df = pd.DataFrame(data_dict, index = [0])
            df = df.append(data_dict, ignore_index = True)

    return df.fillna(0)

def generate_tf_idf(obj_arr):
    # General empy word -> tf_idf matrix
    column_names = ["word"] + [str(o.id) for o in obj_arr]
    df = pd.DataFrame(columns = column_names)

    # Get document frequency matrix
    freq_df = gen_doc_freq(obj_arr)

    # Iterate over each doc and assign values
    for obj in obj_arr: 
        current_index = str(obj.id)
        term_freq_df = gen_term_freq(obj.wordList)
        word_series = term_freq_df["word"]

        for word in word_series.values:
            tf = calc_tf(term_freq_df[term_freq_df["word"] == word]["freq"].values[0])
            idf = calc_idf(len(obj_arr) , freq_df[freq_df["word"] == word]["doc_freq"].values[0])
            tf_idf =  tf * idf
            # If already in df just update tf_idf value
            if word in df["word"].values:
                df.loc[df["word"] == word, "tf_idf"] = tf_idf
                continue
            data_dict = {}
            data_dict["word"] = word
            data_dict[current_index] = tf_idf
            new_row_df = pd.DataFrame(data_dict, index = [0])
            df = df.append(data_dict, ignore_index = True)
    return df.fillna(0)


