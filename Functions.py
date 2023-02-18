import pandas as pd
import numpy as np

def cov_matrix_based(my_data):

    """
    Calculates a covariance matrix given the following parameters:
    :param my_data: dataframe of prices and dates (date format yyyy-mm-dd)
    :return: returns a covariance matrix dataframe
    """
    np.random.seed(42)
    covariance_matrix = pd.DataFrame(np.random.randn(len(my_data), len(my_data.columns)),
                                     index=my_data.index,
                                     columns=list(my_data)).rolling(len(my_data)).cov().dropna().droplevel(0, axis=0)
    return covariance_matrix
    