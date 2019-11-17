import os
import time 

from ResultWritter import ResultWritter


class DownloadReqRunner():
    def __init__(self):
        pass 

    def benchmark_download(self, bucket_name, file_name, dump_path, csv_name):
        start_time = time.perf_counter()
        writer = ResultWritter()
        os.system("aws s3 cp s3://{}/{} {}/{}".format(
            bucket_name,
            file_name,
            dump_path,
            file_name
        ))
        result = time.perf_counter() - start_time
        writer.log_result(bucket_name, result, csv_name)
        return result


        


