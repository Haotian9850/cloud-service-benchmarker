import timeit 
import os

def benchmark_individual_upload(file_name, parent_path, s3_region, bucket_name):
    return timeit.timeit(
        stmt="os.system('aws s3 cp {}/{} s3://{}/')".format(
                parent_path,
                file_name,
                bucket_name
            ),
        setup="import os",
        number=1
    )
