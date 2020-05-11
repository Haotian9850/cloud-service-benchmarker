from pandas import read_csv, DataFrame, concat, Series
import pandas as pd
import time
from datetime import datetime 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn import linear_model
from sklearn.svm import SVC
from sklearn.metrics import make_scorer
import numpy as np

TEST_CSV = "/Users/haotian/Documents/documents-local/cloud-service-benchmarker/results_multi_local_clients_multiple_bucket/ucsd_geni/batch_2/results_pc1.instageni.ucsd.edu_25410_51200kb.csv"


BUCKET = "hao-us-east-1"

def parse_time(raw):
    return datetime.strptime(raw, "%Y-%m-%d %H:%M:%S.%f")

def timeseries_to_supervised(raw, lag=1):
    df = DataFrame(raw)
    cols = [df.shift(i) for i in range(1, lag+1)]
    cols.append(df)
    df = concat(cols, axis=1)
    df.fillna(0, inplace=True)
    df.drop(df.columns[[0, 2]], axis=1, inplace=True)
    return df

def get_total_sec(raw_time)->int:
    return (datetime.strptime(str(raw_time), "%Y-%m-%d %H:%M:%S.%f") - datetime.strptime("-".join(str(raw_time).split()[0].split("-")[:2]), "%Y-%m")).total_seconds()

# within 5% of ground truth
def custom_loss_func(true, pred):
    return abs(pred - true) < 0.05 * true

def custom_score(y_test, y_pred):
    if len(y_pred) != len(y_test):
        raise ValueError("Test and pred set size do not match!")
    err = 0
    for i, pred in enumerate(y_pred):
        if not custom_loss_func(y_test[i], pred):
            err += 1
    return (len(y_test) - err) / len(y_test)



if __name__ == "__main__":
    raw = read_csv(
        TEST_CSV,
        names=["time", "bucket", "result"],
        parse_dates=[0],
        date_parser=parse_time,
        skiprows=5
    )
    raw.drop(raw[raw.bucket != BUCKET].index, inplace=True)
    raw["time"] = raw["time"].map(lambda x : get_total_sec(x))
    X = raw.drop(columns=["result"])
    y = raw["result"]
    X = pd.get_dummies(X)
    '''
    pipeline = ColumnTransformer(
        remainder="passthrough",
        transformers=[("full", Pipeline([
            ("scaler", StandardScaler())
        ]), ["time"])
    ])
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    clf = linear_model.BayesianRidge()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(custom_score(np.array(y_test).tolist(), np.array(y_pred).tolist()))

    plt.plot(
        np.array(X_train["time"]).tolist(), 
        np.array(y_train).tolist(),
        label="X_train"
    )
    plt.plot(
        np.array(X_test["time"]).tolist(), 
        np.array(y_pred).tolist(),
        label="prediction"
    )
    plt.plot(
        np.array(X_test["time"]).tolist(), 
        np.array(y_test).tolist(),
        label="ground_truth"
    )
    plt.xlabel("Month-based time (s)")
    plt.ylabel("Latency (s)")
    plt.savefig("batch_2.png")
    plt.legend(loc='upper left', borderaxespad=0.)
    plt.show()
