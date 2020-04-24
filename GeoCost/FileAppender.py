import logging 
import os 


class FileAppender(object):
    def __init__(self, **kwargs):
        self.num_partitions = kwargs.get("num_paritions", 12)
        self.temp_path = kwargs.get("temp_path", "./temp")
        self.logger = logging.getLogger(__name__)

    def get_file(self, filename):
        pass 

    def _merge_partitions(self, filename):
        partitions = ["{}_{}.{}".format(
            os.path.basename(filename),
            i,
            os.path.splitext(filename)[1]
        ) for i in range(self.num_partitions)]
        with open(filename, "w+") as fin:
        for partition in partitions:
            with open("{}/{}".format(self.temp_path, partition)) as fout:
                for line in fout:
                    fout.write(line)
    

