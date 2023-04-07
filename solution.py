import pandas as pd
import numpy as np


chat_id = 1141722952

def solution(x: np.array) -> float:
    # a = v/time, v - speed
    time = 10 
    n = len(x)
    for i in range(len(x)):
        sum_ai = x[i]/time
    a = (1/n) * sum_ai
    return a
