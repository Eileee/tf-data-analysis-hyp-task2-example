import pandas as pd
import numpy as np
import scipy.stats as st

chat_id = 417796486 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    pv = st.ks_2samp(x,y, alternative ='two-sided')[1]
    if (pv < 0.09):
        return True
    else:
        return False# Ваш ответ, True или False
