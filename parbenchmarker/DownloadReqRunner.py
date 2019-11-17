import os
import time 


class DownloadReqRunner():
    def __init__(self):
        pass 

    def benchmark_download(self, bucket_name, file_name, dump_path):
        start_time = time.perf_counter()
        os.system("aws s3 cp s3://{}/{} {}/{}".format(
            bucket_name,
            file_name,
            dump_path
        ))
        return time.perf_counter() - start_time()
        

        


