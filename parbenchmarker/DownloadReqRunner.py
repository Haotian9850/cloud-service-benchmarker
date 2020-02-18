import os
import time 
from concurrent.futures import ThreadPoolExecutor, as_completed

from ResultWriter import ResultWriter


class DownloadReqRunner():
    def __init__(self):
        self.result_writer = ResultWriter()

    def benchmark_download_job(self, bucket_name, file_name, dump_path, csv_name, is_multi_client=False, gap_sec=0.2):
        if is_multi_client:
            time.sleep(gap_sec)
        start_time = time.perf_counter()
        os.system("aws s3 cp s3://{}/{} {}/{}".format(
            bucket_name,
            file_name,
            dump_path,
            file_name
        ))
        result = time.perf_counter() - start_time
        self.result_writer.log_result(bucket_name, result, csv_name)
        return result


    # multiple client requesting file download with a small time gap (< 1s)
    def benchmark_download_multiple_clients(self, bucket_name, file_name, dump_path, csv_name, num_client, gap_sec, job_callable):
        result = list()
        with ThreadPoolExecutor(max_workers=num_client) as t:
            all_jobs = [
                j.submit(
                    job_callable,
                    bucket_name=bucket_name,
                    file_name=file_name,
                    dump_path=dump_path,
                    csv_name=csv_name,
                    is_multi_client=True,
                    gap_sec
                ) for _ in range(num_client)
            ]
            for future in as_completed(all_jobs):
                result.append(future.result())
        return result






        

        


