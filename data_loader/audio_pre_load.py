from decouple import config
import gdown

from base.base_data_loader import BaseDataLoader


class AudioPreLoad(BaseDataLoader):
    def __init__(self, config):
        super(AudioPreLoad, self).__init__(config)
        self.audio = []


    def download_data_from_google(self):
        gdown.download_folder(url=config('GOOGLE_DRIVE', default=''), 
                              output=self.config.location.audios,
                              quiet=False, 
                              use_cookies=False
                              )
