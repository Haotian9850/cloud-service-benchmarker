import logging

class CloudStorageUploader(object):
    def __init__(self, **kwargs):
        self.service = kwargs.get("service", None)
        self.data_centers = kwargs.get("data_centers", list())
        self.logger = logging.getLogger(__name__)

    def upload(self, path):
        return self._upload(path)
