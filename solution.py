import pandas as pd
import numpy as np
import math
from statistics import mean 


chat_id = 1141722952

def solution(x: np.array) -> float:
    mu = -39 + math.exp(1)
    sample_size = len(x)
    t = 10
    a = []
    for i in range(1, sample_size):
        a.append((x[i] - x[i-1])/t)
    return mean(a)
