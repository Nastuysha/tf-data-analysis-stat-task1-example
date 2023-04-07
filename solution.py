import pandas as pd
import numpy as np


chat_id = 1141722952

def solution(x: np.array) -> float:
    time = 10 
    for i in range(len(x)):
        x[i] /= (time)
    a = np.mean(x)
    return a
