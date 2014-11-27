"""Contains basic finance formulas"""
__author__ = 'Ryan Sorenson'

import sys
import pandas as pd


def fv_analytic(t, initial, monthly_contribution, interest_rate):
    """
    Function returns the analytical solution for the interest rate.

    :param t: Time in months
    :param initial: Initial amount
    :param monthly_contribution: Monthy contribution
    :param interest_rate: Annualized interest rate
    :return: future value
    """

    monthly_interest = interest_rate/12
    return initial * (1 + monthly_interest) ** t + \
        monthly_contribution * (1 + monthly_interest) * ((1 + monthly_interest) ** t - 1) / interest_rate


def fv_pretty(t, initial, monthly_contribution, interest_rate, html=False):
    #TODO: Add decent test here
    """
    Gives us ammoratized compound interest in pretty formats

    :param t: Time in months
    :param initial: Initial amount
    :param monthly_contribution: monthly investment
    :param interest_rate:
    :return pd.Series or HTML table containing the month numbers and the current
    Acummulated savings

    """

    # Skip the month before contributions.
    df = pd.DataFrame(fv_iterated(t=t, initial=initial, monthly_contribution=monthly_contribution,
                                  interest_rate=interest_rate), columns=['Month', 'Value'])[1:]

    df = df.set_index('Month')

    if html:
        return df.to_html().replace("\n", "")
    else:
        return df


def fv_iterated(t, initial, monthly_contribution, interest_rate):
    # http://stackoverflow.com/questions/21543017/compound-interest-with-deposits-in-python
    """
    Gives ammortized savings. Note that we assume that returns are
    compounded monthly and that the savings are made at the start
    of each month

    :param t: Time in months
    :param initial: Initial amount
    :param monthly_contribution: monthly investment
    :param interest_rate:
    :return: tuples containg the values with the interest rate


    >>> values = fv_iterated(12, 20000, 2000, .12)
    >>> round(values[-1][1])
    45678.0
    """
    monthly_interest = interest_rate/12

    values = [tuple([0, initial])]

    for month in range(t)[1:]:
        values.append(tuple([month, (values[-1][1] + monthly_contribution)*(1+ monthly_interest)]))

    return values
