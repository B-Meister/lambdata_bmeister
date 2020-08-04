"""
Lambdata - A shareable package to help clean data in dataframes
"""

import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split


def data_to_clean(df):
    """
    Looks at a dataframe and tells you what needs to be cleaned
    :param df: Takes data
    :return:
    """
    null_values = df.isnull().sum()
    return null_values


def split(df):
    """
    Splits the given dataframe into a 8/2 split for training and testing
    :param df:the dataframe you want to split
    :return:
    """
    training, test = train_test_split(df, test_size=0.2, random_state=42)
    train, val = train_test_split(training, test_size=0.2, random_state=42)

    return train.shape, valshape, test.shape


print("All ready to run")

Test = pd.DataFrame(np.ones(10))
