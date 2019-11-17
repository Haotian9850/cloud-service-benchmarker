import matplotlib 
import matplotlib.pyplot as plt 
import pandas as pd

def plot_latency(raw_data):
    df = pd.DataFrame(raw_data)
    print(df)
    df.plot.bar(rot=0)
    plt.ylabel("Latency (s)")
    plt.xlabel("Test file (KB)")
    plt.savefig("multi_client_20.png", dpi=300)
    plt.show()









    
