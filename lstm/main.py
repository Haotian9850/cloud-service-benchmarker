from pandas import read_csv, DataFrame, concat, Series
from datetime import datetime 
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

import numpy as np

TEST_CSV = "/Users/haotian/Documents/documents-local/cloud-service-benchmarker/results_multi_local_clients_multiple_bucket/24_hr/results_pc604.emulab.net_26274_8kb.csv"


BUCKET = "hao-us-east-1"

def parse_time(raw):
    return datetime.strptime(raw, "%Y-%m-%d %H:%M:%S.%f")

def load_csv(path):
    result = read_csv(
        path,
        names=["time", "bucket", "result"],
        parse_dates=[0],
        date_parser=parse_time
    )
    return result

def timeseries_to_supervised(raw, lag=1):
    df = DataFrame(raw)
    cols = [df.shift(i) for i in range(1, lag+1)]
    cols.append(df)
    df = concat(cols, axis=1)
    df.fillna(0, inplace=True)
    df.drop(df.columns[[0, 2]], axis=1, inplace=True)
    return df

def difference(raw, interval=1):
    diff = list()
    for i in range(interval, len(raw)):
        val = raw[i] - raw[i - interval]
        diff.append(val)
    diff_df = DataFrame(diff)
    diff_df.drop(diff_df.columns[[0]], axis=1, inplace=True)
    return diff_df

def inv_difference(history, yhat, interval=1):
    return yhat + history[-interval]

if __name__ == "__main__":
    data = load_csv(TEST_CSV)
    data.drop(data[data["bucket"] != BUCKET].index, inplace=True)
    data.drop("bucket", 1, inplace=True)
    print(data.head())
    data.set_index("time").plot()
    #data.plot()
    pyplot.show()
    '''
    X = data["time"]
    y = data["result"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, shuffle=False, test_size=0.2
    )
    print(X.head())
    print(X_train.shape)
    print(y_train.shape)
    supervised = timeseries_to_supervised(data.values, 1)
    print(supervised.head())
    diffed = difference(supervised.values, 1)
    print(diffed.head())
    print(X)
    X = np.array(X)
    X = X.reshape(len(X), 1)
    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler = scaler.fit(X)
    scaled_X = scaler.transform(X)
    print(scaled_X)
    '''
