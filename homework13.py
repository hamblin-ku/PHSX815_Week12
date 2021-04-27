# File:     minimize.py
# Author:   Kurt Hamblin
# Description:  Utitlize the Random Class to:
# Simulate dice rolls where the dice weights are sampled from a Rayleigh Distribution

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from Random import Random
import matplotlib
import seaborn as sns

# Import my custom matplotlib config and activate it
import my_params
custom_params = my_params.params()
matplotlib.rcParams.update(custom_params)


if __name__ == "__main__":

    sigma = 1
    rand = Random(seed = 5555)
    
    Nexp = 100
    n = 500
    
    exp_results = np.zeros(Nexp)
    
    for i in np.arange(Nexp):
        exp_tot = 0
        for j in np.arange(n):
            exp_tot += rand.Rayleigh(sigma)
        exp_results[i] = exp_tot / n
    
    ax = sns.distplot(exp_results)
    ax.set_xlabel('Sample Average')
    
    
    plt.show()
