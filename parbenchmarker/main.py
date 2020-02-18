#!/usr/bin/env python3

import schedule
import time
import os
import datetime


from FileMaker import FileMaker
from ConfigReader import ConfigReader
from DownloadReqRunner import DownloadReqRunner

USERNAME = "hl7gr"

CONFIG_PATH = "/users/{}/parbenchmarker/config.yaml".format(USERNAME)
TEST_FILE_PREDIX = "test"
TEST_FILE_PARENT_PATH = "/users/{}/parbenchmarker/data".format(USERNAME)
DUMP_PATH = "/users/{}/parbenchmarker/dump".format(USERNAME)
RESULT_CSV = "/users/{}/parbenchmarker/results.csv".format(USERNAME)


def download_benchmarking_job(bucket, file_name, dump_path, csv_name):
    print(DownloadReqRunner().benchmark_download_job(
        bucket,
        file_name,
        dump_path,
        csv_name
    ))

def upload_test_file(bucket, file_name, parent_path):
    os.system("aws s3 cp {}/{} s3://{}/".format(
        parent_path,
        file_name,
        bucket
    ))

def generate_job_times(start_time, num_buckets, gap_sec):
    result = list()
    result.append(start_time)
    start = datetime.datetime.strptime(start_time, "%H:%M:%S")
    for i in range(num_buckets - 1):
        start = start + datetime.timedelta(0, gap_sec)
        result.append(datetime.datetime.strftime(start, "%H:%M:%S"))
        i += 1
    return result




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
    req_times = generate_job_times(config["start_time"], len(config["buckets"]), config["gap_sec"])
    for i in range(len(config["buckets"])):
        print(config["buckets"][i])
        schedule.every().day.at(req_times[i]).do(
            download_benchmarking_job,
            bucket=config["buckets"][i],
            file_name=test_file,
            dump_path=DUMP_PATH,
            csv_name=RESULT_CSV
        )
    while True:
        schedule.run_pending()
        
    





    
