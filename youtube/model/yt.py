from youtube.settings import CAPTIONS_DIR
from youtube.settings import VIDEOS_DIR
import os


class yt:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id(url)
        self.captionFilepath = self.get_caption_filepath()
        self.videoFilepath = self.get_video_filepath()
        self.captions = None
        self.time_start = None
        self.time_duration = None
        self.download_or_not = False

    @staticmethod  # 如果這個function不需要用到別的function或參數(不需要self)就可以用staticmethod
    def get_video_id(url):
        return url.split('watch?v=')[-1]

    def get_caption_filepath(self):
        return os.path.join(CAPTIONS_DIR, self.id + '.txt')

    def get_video_filepath(self):
        return os.path.join(VIDEOS_DIR, self.id + '.mp4')
