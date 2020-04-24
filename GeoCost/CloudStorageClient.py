import logging

class CloudStorageClient(object):
    def __init__(self, **kwargs):
        self.service = kwargs.get("service", None)
        self.data_centers = kwargs.get("data_centers", list())
        self.client = None
        self.temp_path = kwargs.get("temp_path", "./temp")
        self.logger = logging.getLogger(__name__)

    def upload(self, path):
        # to be overridden by sub class
        pass

    def download(self, path):
        # to be overriden by sub class
        pass

