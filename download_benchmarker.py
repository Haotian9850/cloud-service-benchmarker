import timeit 
import os

def benchmark_individual_download(file_name, parent_path, s3_region, bucket_name):
    return timeit.timeit(
        stmt="os.system('aws s3 cp s3://{}/{} {}/{}')".format(
                bucket_name,
                file_name,
                parent_path,
                file_name,
            ),
        setup="import os",
        number=1
    )


