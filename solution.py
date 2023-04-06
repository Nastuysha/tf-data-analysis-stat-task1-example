import pandas as pd
import numpy as np


chat_id = 1141722952  # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 10
    return (2 / t**2) * np.mean(x)
