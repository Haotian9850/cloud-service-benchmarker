#!/usr/bin/env python3

import schedule
import time
import os
import datetime
import logging, logging.config


from FileMaker import FileMaker
from ConfigReader import ConfigReader
from DownloadReqRunner import DownloadReqRunner

USERNAME = "hl7gr"

'''
CONFIG_PATH = "/users/{}/parbenchmarker/config.yaml".format(USERNAME)
TEST_FILE_PREFIX = "test"
TEST_FILE_PARENT_PATH = "/users/{}/parbenchmarker/data".format(USERNAME)
DUMP_PATH = "/users/{}/parbenchmarker/dump".format(USERNAME)
RESULT_CSV = "/users/{}/parbenchmarker/results.csv".format(USERNAME)
'''
CONFIG_PATH = "./config.yaml"
TEST_FILE_PREFIX = "test"
TEST_FILE_PARENT_PATH = "./data"
DUMP_PATH = "./dump"
RESULT_CSV = "./results.csv"


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{levelname} {asctime}]    {module} {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "verbose"
            }
        },
        "loggers": {
            "": {
                "handlers": ["console"],
                "level": "INFO"
            }
        }
    }

logging.config.dictConfig(LOGGING_CONFIG)

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
        TEST_FILE_PREFIX,
        TEST_FILE_PARENT_PATH,
    )
    for bucket in config["buckets"]:
        logging.info("Uploading test file {} to bucket {}...".format(test_file, bucket))
        upload_test_file(bucket, test_file, TEST_FILE_PARENT_PATH)
    req_times = generate_job_times(config["start_time"], len(config["buckets"]), config["gap_sec"])
    for i in range(len(config["buckets"])):
        logging.info("Benchmarking bucket {} with test file size {} kb...".format(config["buckets"][i], config["file_size_kb"]))
        if config["multi_local_clients"]:
            schedule.every().day.at(req_times[i]).do(
                runner.benchmark_download_multiple_clients,
                bucket_name=config["buckets"][i],
                file_name=test_file,
                dump_path=DUMP_PATH,
                csv_name=RESULT_CSV,
                num_client=config["num_local_clients"],
                gap_sec=config["between_req_sec"],
                job_callable=runner.benchmark_download_job
            )
        schedule.every().day.at(req_times[i]).do(
            runner.benchmark_download_job,
            bucket_name=config["buckets"][i],
            file_name=test_file,
            dump_path=DUMP_PATH,
            csv_name=RESULT_CSV
        )
    while True:
        schedule.run_pending()
        
    





    
