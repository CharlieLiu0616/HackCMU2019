import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy
import os
import csv
numpy.random.seed(7)

dict_stock = {"1":"FLEX.csv"}

date = 10

def MLHelper(stock_name):
    real_name = dict_stock[stock_name]
    df = pd.read_csv(os.path.join("result",real_name), usecols = [0,1])
    return(df.values[date-1].item(1))
