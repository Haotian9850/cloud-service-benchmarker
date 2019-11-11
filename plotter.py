import matplotlib 
import matplotlib.pyplot as plt 
import pandas as pd

def plot_latency(raw_data):
    df = pd.DataFrame(raw_data)
    print(df)
    df.plot.bar(rot=0)
    plt.xlabel("Latency (s)")
    plt.ylabel("Test file")
    plt.show()









    
