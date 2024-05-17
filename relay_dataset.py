import random
import numpy as np
import pandas as pd


data = {
    'time' : [random.randint(0, 100) for _ in range(1000)],
    'distance' : [random.randint(0, 6) for _ in range(1000)],
    'strength' : [random.randint(50, 120) for _ in range(1000)]
}

data = pd.DataFrame(data)
data.to_csv('normal.csv')