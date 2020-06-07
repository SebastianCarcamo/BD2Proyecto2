import pandas as pd
import numpy as np

def cos_similarity(a, b):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def calc_cos_similar(df, doc_id_1, doc_id_2): 
    vec_1 = df[doc_id_1].to_numpy()   
    vec_2 = df[doc_id_2].to_numpy()   
    return cos_similarity(id_1_val, id_2_val)
