from download_benchmarker_multi_client import benchmark_concurrent_download
from config_reader import read_config
from file_maker import make_file
from plotter import plot_latency

import os


CONFIG_FILE_PATH = "config.yaml"
DATA_PARENT_PATH = "data/"
DUMP_PATH = "dump/"
TEST_FILE_NAME_GENERIC = "test"


def benchmark_multi_client():
    benchmark_configuration = read_config(CONFIG_FILE_PATH)
    test_files = [make_file(size, TEST_FILE_NAME_GENERIC, DATA_PARENT_PATH) for size in benchmark_configuration["file_size_kb"]]
    for file_name in test_files:
        for bucket in benchmark_configuration["buckets"]:
            os.system("aws s3 cp {}/{} s3://{}/".format(
                DATA_PARENT_PATH,
                file_name,
                bucket
            ))
    result = dict()
    for i in range(len(benchmark_configuration["regions"])):
        result[benchmark_configuration["regions"][i]] = dict()
        for file_name in test_files:
            result[benchmark_configuration["regions"][i]][file_name] = benchmark_concurrent_download(
                file_name,
                DUMP_PATH,
                benchmark_configuration["buckets"][i],
                benchmark_configuration["num_clients"]
            )
    plot_latency(result)
    return result


if __name__ == "__main__":
    benchmark_multi_client()


    