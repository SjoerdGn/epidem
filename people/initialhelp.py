import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF 
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))
agesex = pd.read_csv("../data/people/agesex.csv", delimiter=';')

agesex = agesex.rename(columns = {'Leeftijd':'age', 'Geslacht':'sex',
                                  'Bevolking (aantal)':'num'})


agesex['age'] = agesex['age'].str.strip(' jaar').astype(int)
agesex = agesex.set_index('age')

agesex = agesex.drop(['Burgerlijke staat', 'Perioden'], axis = 1)
men = agesex[agesex['sex']=='Mannen'].drop('sex', axis = 1)
women = agesex[agesex['sex']=='Vrouwen'].drop('sex', axis = 1)

menecdf = ECDF(men.values.T[0])
womenecdf = ECDF(women.values.T[0])
