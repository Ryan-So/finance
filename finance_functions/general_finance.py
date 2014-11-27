"""Description Here"""
__author__ = 'Ryan Sorenson'

##TODO double check that math is correct since rewriting into months

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
    """

    :param t: Time in months
    :param initial: Initial amount
    :param monthly_contribution: monthly investment
    :param interest_rate:
    :return pd.Series or HTML table containing the
    """

    df = pd.DataFrame(fv_iterated(t=t, initial=initial, monthly_contribution=monthly_contribution,
                                  interest_rate=interest_rate))

    if html:
        return df.to_html.replace("\n", "")
    else:
        return df


def fv_iterated(t, initial, monthly_contribution, interest_rate):
    # http://stackoverflow.com/questions/21543017/compound-interest-with-deposits-in-python
    pass
