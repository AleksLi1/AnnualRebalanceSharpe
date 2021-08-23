import pandas as pd
import numpy as np
from datetime import datetime, date


def annual_cov(period, my_date, my_data, tickers):

    """
    Calculates a covariance matrix given the following parameters:
    :param period: training period in years, int
    :param my_date: first day of the trading year, str
    :param my_data: dataframe of prices and dates
    :param tickers: list of tickers
    :return: returns a covariance matrix dataframe
    """

    covariance_matrix = pd.DataFrame(np.random.randn(252*period, len(tickers)),
                                     index=pd.date_range(my_date, periods=252*period),
                                     columns=list(my_data)).rolling(252*period).cov().dropna().droplevel(0, axis=0)
    return covariance_matrix


def start_date(my_date):

    """
    Gives the starting date of a month given any date
    :param my_date: date, str
    :return: str
    """

    my_date = datetime.strptime(my_date, '%Y-%m-%d')
    starting_date = date(my_date.year, 1, 1)
    starting_date = starting_date.strftime('%Y-%m-%d')
    return starting_date


def start_of_month(my_date):

    """
    Gives the starting date of a month given any date
    :param my_date: date, str
    :return: str
    """

    my_date = datetime.strptime(my_date, '%Y-%m-%d')
    starting_date = date(my_date.year, my_date.month, 1)
    starting_date = starting_date.strftime('%Y-%m-%d')
    return starting_date

