import game_of_life as gol
import numpy as np
import pandas as pd
import glob

for csv in glob.glob('*.csv'):
    print(csv)
    df =  pd.read_csv(csv)
    matrix  = df.values
    gol.savethematrizen(gol.spiel(matrix), csv)
    #print(f"das csv {csv } lautet \n {nnp} \n \n")


#gol.savethematrizen(gol.spiel(np.array([1,2,3,4,5,6,7,8,9]*4).reshape(6,6)),"test2")


