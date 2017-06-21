import pandas as pd


def equal_operator(ds1, ds2):
    ds = (ds1 == ds2)
    return ds


def greater_than_operator(ds1, ds2):
    ds = (ds1 > ds2)
    return ds


def less_than_operator(ds1, ds2):
    ds = (ds1 < ds2)
    return ds

input1 = pd.Series([2, 4, 6, 8, 10])
input2 = pd.Series([1, 3, 5, 7, 10])

equal_operator(input1,input2)
greater_than_operator(input1,input2)
less_than_operator(input1,input2)
