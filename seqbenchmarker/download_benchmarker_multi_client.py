from concurrent.futures import ThreadPoolExecutor
import os 
import time




def benchmark_concurrent_download(file_name, parent_path, bucket_name, num_clients):
    start_time = time.perf_counter() #CPU time, process-independent
    with ThreadPoolExecutor(num_clients) as executor:
        executor.map(os.system, ["aws s3 cp s3://{}/{} {}/{}".format(bucket_name, file_name, parent_path, file_name) for i in range(num_clients)])
    return time.perf_counter() - start_time


    

