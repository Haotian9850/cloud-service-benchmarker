import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

from Results import Results

if __name__ == "__main__":
    df = pd.DataFrame({
        "1 KB Split": Results.RESULT_1KB_SPLIT.value,
        "10 KB Split": Results.RESULT_10KB_SPLIT.value,
        "1 MB Split": Results.RESULT_1MB_SPLIT.value,
        "10MB Split": Results.RESULT_10MB_SPLIT.value,
        "50MB Split": Results.RESULT_50MB_SPLIT.value,
        "1 KB Single": Results.RESULT_1KB_SINGLE.value,
        "10 KB Single": Results.RESULT_10KB_SINGLE.value,
        "1 MB Single": Results.RESULT_1MB_SINGLE.value,
        "10 MB Single": Results.RESULT_10MB_SINGLE.value,
        "50 MB Single": Results.RESULT_50MB_SINGLE.value
    })
    df.to_csv("single_vs_split.csv")
    fig = df.plot(
        title="Single vs. splitted downloading latency",
        figsize=(15, 10)
    )
    fig.set_xlabel("No. requests")
    fig.set_ylabel("Downloading latency (s)")
    fig.get_figure().savefig("single_vs_split.png")    
    plt.show()