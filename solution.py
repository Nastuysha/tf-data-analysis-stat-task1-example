import pandas as pd
import numpy as np
import math

chat_id = 1141722952

def solution(x: np.array) -> float:
    mu = -39 + math.exp(1)
    sample_size = len(x)
    V0 = x[0]
    ch = 0
    zn = 0
    t = 10
    for i in range(sample_size):
        ch += (x[i]-V0)
        zn += (t - mu)
    a = ch/zn
    return a
