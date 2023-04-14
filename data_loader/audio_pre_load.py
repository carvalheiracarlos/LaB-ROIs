import gdown

from base.base_data_loader import BaseDataLoader


class AudioPreLoad(BaseDataLoader):
    def __init__(self, config):
        super(AudioPreLoad, self).__init__(config)
        self.audio = []


    def download_data_from_google(self):
        gdown.download_folder(self.config.google.repository.folder, quiet=False, use_cookies=False)
