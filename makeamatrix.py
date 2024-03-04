import pandas as pd
import numpy as np
import glob

#A = np.matrix([[2,2],[4,5]])

A = np.array([1,2,3,4,5,6,7,8,9]*4).reshape(6,6)
df = pd.DataFrame(A)
df.to_csv("one.csv")




A = np.array([1,2,3,4]*4).reshape(4,4)
df = pd.DataFrame(A)
df.to_csv("two.csv")

