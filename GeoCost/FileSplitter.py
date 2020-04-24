import logging
import os

class FileSplitter(object):
    def __init__(self, **kwargs):
        self.num_partitions = kwargs.get("num_partition", 12)
        self.temp_path = kwargs.get("temp_path", "./temp")
        self.logger = logging.getLogger(__name__)        

    def split_and_save(self, path):
        if not os.path.exists(self.temp_path):
            os.makedirs(self.temp_path)
        self._split_in_parts(path)
        
    
    def _get_filename(self, path:str):
        return os.path.basename(path)
    

    def _split_in_parts(self, path:str):
        size_byte = -1
        partition_byte = -1
        try:
            size_byte = os.path.getsize(path)
            partition_byte = size_byte // self.num_partitions
        except OSError as e:
            self.logger.error("Cannot split file {}: {}".format(path, str(e)))
        with open(path, "rb") as fin:
            raw_bytes = bytearray(size_byte)
            fin.readinto(raw_bytes)
            for p, i in enumerate(range(0, len(raw_bytes), partition_byte)):
                with open("{}/{}_{}".format(self.temp_path, self._get_filename(path), p), "wb+") as fout:
                    fout.write(raw_bytes[i : i + partition_byte])

if __name__ == "__main__":
    f = FileSplitter()
    f.split_and_save("test.txt")
        
        