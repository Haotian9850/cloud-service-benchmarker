from concurrent.futures import ThreadPoolExecutor
import os 
import time




def benchmark_concurrent_download(file_name, parent_path, s3_region, bucket_name, num_threads):
    start_time = time.perf_counter() #CPU time, process-independent
    with ThreadPoolExecutor(num_threads) as executor:
        executor.map(os.system, ["aws s3 cp s3://{}/{} {}/{}".format(bucket_name, file_name, parent_path, file_name) for i in range(num_threads)])
    return time.perf_counter() - start_time
    




print(benchmark_concurrent_download("test1024kb", "dump/", "us-east-1", "benchmarking-hao", 5))

    

