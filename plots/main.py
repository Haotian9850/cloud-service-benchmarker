import matplotlib.pyplot as plt 
import pandas as pd

DATA_50MB = pd.read_csv(
    filepath_or_buffer="/Users/haotian/Documents/documents-local/cloud-service-benchmarker/results_multi_local_clients_multiple_bucket/ucsd_geni/batch_2/results_pc1.instageni.ucsd.edu_25410_51200kb.csv",
    names=["time", "bucket", "latency"],
    skiprows=5
)
DATA_75MB = pd.read_csv(
    filepath_or_buffer="/Users/haotian/Documents/documents-local/cloud-service-benchmarker/results_multi_local_clients_multiple_bucket/ucsd_geni/batch_2/results_pc2.instageni.ucsd.edu_25410_76800kb.csv",
    names=["time", "bucket", "latency"],
    skiprows=5
)
DATA_100MB = pd.read_csv(
    filepath_or_buffer="/Users/haotian/Documents/documents-local/cloud-service-benchmarker/results_multi_local_clients_multiple_bucket/ucsd_geni/batch_2/results_pc3.instageni.ucsd.edu_25410_102400kb.csv",
    names=["time", "bucket", "latency"],
    skiprows=5
)

SELECTED_BUCKET = "hao-us-east-1"

ALL_BUCKETS = [
    "hao-us-east-1",
    "hao-ap-southeast-2",
    "hao-ap-northeast-1",
    "hao-eu-west-2",
    "hao-sa-east-1",
    "hao-ca-central-1",
    "hao-us-west-1"
]


def extract_single_bucket(df):
    temp =  df.drop(df[df.bucket != SELECTED_BUCKET].index, inplace=False)
    return temp.drop(labels=["bucket"], axis=1, inplace=False)

def plot_single_bucket():
    data_50mb_clean = extract_single_bucket(DATA_50MB)
    data_75mb_clean = extract_single_bucket(DATA_75MB)
    data_100mb_clean = extract_single_bucket(DATA_100MB)
    fig = data_50mb_clean.plot(
        title="Time-series latency of different file sizes",
        figsize=(15, 10),
        lw=1
    )
    data_75mb_clean.plot(ax=fig)
    data_100mb_clean.plot(ax=fig)
    fig.legend(["50 MB", "75 MB", "100 MB"])
    fig.set_xlabel("Time")
    fig.set_ylabel("Downloading latency (s)")
    fig.get_figure().savefig("single_bucket.png")
    plt.show()


def extract_first_req(df):
    drop_index = list()
    for i in range(len(df["latency"])):
        if i % 5 != 0:
            drop_index.append(i)
    return df.drop(drop_index, inplace=False)

def plot_all_buckets_single_client_avg():
    means_50mb = extract_first_req(DATA_50MB).groupby("bucket").mean().reset_index()["latency"].tolist()
    means_75mb = extract_first_req(DATA_75MB).groupby("bucket").mean().reset_index()["latency"].tolist()
    means_100mb = extract_first_req(DATA_100MB).groupby("bucket").mean().reset_index()["latency"].tolist()
    index = ALL_BUCKETS
    df = pd.DataFrame({
        "50 MB": means_50mb,
        "75 MB": means_75mb,
        "100 MB": means_100mb
    }, index=index)
    fig = df.plot.bar(
        rot=0,
        title="Averge download latency of all major S3 datacenters",
        figsize=(15, 10)
    )
    fig.set_xlabel("Bucket")
    fig.set_ylabel("Averge downloading latency (s)")
    fig.get_figure().savefig("all_bucket_single_client_avg.png")
    plt.show()


def plot_all_buckets_avg():
    means_50mb = DATA_50MB.groupby("bucket").mean().reset_index()["latency"].tolist()
    means_75mb = DATA_75MB.groupby("bucket").mean().reset_index()["latency"].tolist()
    means_100mb = DATA_100MB.groupby("bucket").mean().reset_index()["latency"].tolist()
    index = ALL_BUCKETS
    df = pd.DataFrame({
        "50 MB": means_50mb,
        "75 MB": means_75mb,
        "100 MB": means_100mb
    }, index=index)
    fig = df.plot.bar(
        rot=0,
        title="Averge download latency of all major S3 datacenters (5 concurrent client requests)",
        figsize=(15, 10)
    )
    fig.set_xlabel("Bucket")
    fig.set_ylabel("Averge downloading latency (s)")
    fig.get_figure().savefig("all_bucket_avg.png")
    plt.show()



if __name__ == "__main__":
    #plot_single_bucket()
    #plot_all_buckets_avg()
    plot_all_buckets_single_client_avg()