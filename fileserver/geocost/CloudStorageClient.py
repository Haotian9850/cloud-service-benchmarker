import logging
import os

from geocost.FileSplitter import FileSplitter
from geocost.FileAppender import FileAppender


class CloudStorageClient(object):
    def __init__(self, **kwargs):
        self.data_centers = kwargs.get("data_centers", list())
        self.client = None
        self.temp_path = kwargs.get("temp_path", "./temp")
        self.access_key = kwargs.get("access_key", None)
        self.secret_key = kwargs.get("secret_key", None)
        self.fsplitter = FileSplitter()
        self.fappender = FileAppender()
        self.logger = logging.getLogger(__name__)

    def upload(self, path):
        # to be overridden by sub class
        pass

    def download(self, path):   
        # to be overriden by sub class
        pass


    def _validate_path(self, path):
        if not os.path.isfile(path):
            raise ValueError("Input path is a directory, not file!")
        if not os.path.exists(path):
            raise ValueError("File {} not found!".format(path))
        try:
            _ = open(path)
        except IOError as e:
            raise RuntimeError("File {} cannot be opened: {}".format(path, str(e)))

    def _validate_credentials(self):
        if not self.access_key:
            raise ValueError("Access key not set!")
        if not self.secret_key:
            raise ValueError("Secret key not set!")

    def _validate_download_pattern(self, raw:list):
        if len(raw) != self.fsplitter.num_partitions:
            raise ValueError("Invalid download pattern shape: {}".format(len(raw)))

        

