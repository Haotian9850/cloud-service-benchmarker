from upload_benchmarker import benchmark_individual_upload
from download_benchmarker import benchmark_individual_download
from config_reader import read_config
from file_maker import make_file

import logging 
logging.basicConfig(
    filename="benchmarker_log.log",
    level=logging.INFO,
    filemode="w"
)



CONFIG_FILE_PATH = "config.yaml"
DATA_PARENT_PATH = "data/"
DUMP_PATH = "dump/"
TEST_FILE_NAME_GENERIC = "test"


def benchmark():
    benchmark_configuration = read_config(CONFIG_FILE_PATH)
    logging.info("Reading config file...")
    test_files = [make_file(size, TEST_FILE_NAME_GENERIC, DATA_PARENT_PATH) for size in benchmark_configuration["file_size_kb"]]
    logging.info("--- Beginning of benchmarking ---")
    for region in benchmark_configuration["regions"]:
        for file_name in test_files:
            logging.info("Uploading file {} to S3 in region {}: {}s".format(
                file_name,
                region,
                benchmark_individual_upload(file_name, DATA_PARENT_PATH, region, benchmark_configuration["bucket"])
            ))
            logging.info("Downloading file {} from S3 in region {}: {}s".format(
                file_name,
                region,
                benchmark_individual_download(file_name, DUMP_PATH, region, benchmark_configuration["bucket"])
            ))
    logging.info("--- End of benchmarking ---")




if __name__ == "__main__":
    benchmark()



