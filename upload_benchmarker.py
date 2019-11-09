import timeit 
import os

def benchmark_individual_upload(file_name, parent_path, s3_region, bucket_name):
    setup = "import os"
    upload_case_template = "os.system('aws s3 cp {}/{} s3://{}/')".format(
        parent_path,
        file_name,
        bucket_name
    )
    return timeit.timeit(
        stmt=upload_case_template,
        setup=setup,
        number=1
    )

print(benchmark_individual_upload(
    "test1kb",
    "/mnt/documents-local/cloud-service-benchmarker/data/",
    "us-east-2",
    "benchmarking-hao"
))