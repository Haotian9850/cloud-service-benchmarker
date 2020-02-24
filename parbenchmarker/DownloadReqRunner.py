import os
import time 
from datetime import datetime
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

from ResultWriter import ResultWriter


class DownloadReqRunner():
    def __init__(self):
        self.result_writer = ResultWriter()
        self.logger = logging.getLogger(__name__)

    def benchmark_download_job(self, bucket_name, file_name, dump_path, csv_name, is_multi_client=False, gap_sec=0.2):
        self.logger.debug("Downloading file {} from s3 bucket {}...".format(
            file_name,
            bucket_name
        ))
        if is_multi_client:
            self.logger.info("sleeping....")
            time.sleep(gap_sec)
        start_time = time.perf_counter()
        os.system("aws s3 cp s3://{}/{} {}/{}".format(
            bucket_name,
            file_name,
            dump_path,
            file_name
        ))
        result = time.perf_counter() - start_time
        self.result_writer.log_result(bucket_name, result, csv_name, datetime.now())
        return result


    # multiple client requesting file download with a small time gap (< 1s)
    def benchmark_download_multiple_clients(self, bucket_name, file_name, dump_path, csv_name, num_client, gap_sec, job_callable):
        result = list()
        with ThreadPoolExecutor(max_workers=num_client) as t:
            all_jobs = [
                t.submit(
                    job_callable,
                    bucket_name=bucket_name,
                    file_name=file_name,
                    dump_path=dump_path,
                    csv_name=csv_name,
                    is_multi_client=True,
                    gap_sec=gap_sec
                ) for _ in range(num_client)
            ]
            for future in as_completed(all_jobs):
                self.logger.info("Task completed: {}".format(future.result()))
                result.append(future.result())
        return result


'''
if __name__ == "__main__":
    d = DownloadReqRunner()
    result = d.benchmark_download_multiple_clients(
        bucket_name="hao-us-east-1",
        file_name="test1kb",
        dump_path="./dump",
        csv_name="./results.csv",
        num_client=5,
        gap_sec=0.2,
        job_callable=d.benchmark_download_job
    )
    print(result)
'''




        

        


