import schedule
import time
import os


from FileMaker import FileMaker
from ConfigReader import ConfigReader
from DownloadReqRunner import DownloadReqRunner

CONFIG_PATH = "./config.yaml"
TEST_FILE_PREDIX = "test"
TEST_FILE_PARENT_PATH = "data"
DUMP_PATH = "dump"


def download_benchmarking_job(bucket, file_name, dump_path):
    print(DownloadReqRunner().benchmark_download(
        bucket,
        file_name,
        dump_path
    ))

def upload_test_file(bucket, file_name, parent_path):
    os.system("aws s3 cp {}/{} s3://{}/".format(
        parent_path,
        file_name,
        bucket
    ))


# Does not have to be exception-tolerant due to small number of jobs
if __name__ == "__main__":
    reader = ConfigReader(CONFIG_PATH)
    maker = FileMaker()
    runner = DownloadReqRunner()
    config = reader.read_config()
    test_file = maker.make_test_file(
        config["file_size_kb"],
        TEST_FILE_PREDIX,
        TEST_FILE_PARENT_PATH,
    )
    for bucket in config["buckets"]:
        upload_test_file(bucket, test_file, TEST_FILE_PARENT_PATH)
    for i in range(len(config["buckets"])):
        print(config["buckets"][i])
        print(config["req_times"][i])
        schedule.every().day.at(config["req_times"][i]).do(
            download_benchmarking_job,
            bucket=config["buckets"][i],
            file_name=test_file,
            dump_path=DUMP_PATH
        )
    while True:
        schedule.run_pending()
        
        
    





    
