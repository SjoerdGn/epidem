import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import os
#os.chdir(os.path.abspath(os.path.dirname(__file__)))
# Source: CBS Statline
agesex = pd.read_csv("../epidem/data/people/agesex.csv", delimiter=';')

agesex = agesex.rename(columns = {'Leeftijd':'age', 'Geslacht':'sex',
                                  'Bevolking (aantal)':'num'})


agesex['age'] = agesex['age'].str.strip(' jaar').astype(int)
agesex = agesex.set_index('age')

agesex = agesex.drop(['Burgerlijke staat', 'Perioden'], axis = 1)
men = agesex[agesex['sex']=='Mannen'].drop('sex', axis = 1)['num']
women = agesex[agesex['sex']=='Vrouwen'].drop('sex', axis = 1)['num']


def _make_ecdf(series):
    cumnum = series.cumsum()
    ecdf = cumnum/np.sum(series)
    return ecdf

menecdf = _make_ecdf(men)
womenecdf = _make_ecdf(women)

def generate_age(sex):
    """Generate the age of a person depending on its sex
    

    Parameters
    ----------
    sex : int
        Sex should be either 0 (men) or 1 (women).

    Raises
    ------
    ValueError
        If sex is not 0 or 1.

    Returns
    -------
    age : int
        Generated age of a person.

    """
    randunif = np.random.rand(1)
    if sex == 0:
        age = menecdf.iloc[(menecdf-randunif).abs().argsort()[:1]].index.tolist()[0]
    elif sex == 1:
        age = womenecdf.iloc[(womenecdf-randunif).abs().argsort()[:1]].index.tolist()[0]
    else:
        raise ValueError("Sex should be either 0 (men) or 1 (women)")
    return age
    