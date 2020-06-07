import pandas as pd
import numpy as np


def generate_tf_idf(obj_arr):
    column_names = ["word", "td", "idf"]
    df = pd.DataFrame(columns = column_names)

    for obj in obj_arr: 
        current_index = obj.index 
        for word in obj.word_vec:
            word_series = df[df["word"] == word]
            if word_series.empty:
                data_dict = {}
                data_dict["word"] = word
                data_dict["tf"] = 1
                data_dict["idf"] = [current_index]
                new_row_df = pd.DataFrame(data_dict, index = [0])
                df = df.append(data_dict, ignore_index = True)
            else:
                if current_index not in df.loc[df["word"] == word, "idf"]:
                    df.loc[df["word"] == word, "tf"] += 1
                    tmp_list = df.loc[df["word"] == word, "idf"].iloc[0]
                    tmp_list.append(current_index)
    return df
