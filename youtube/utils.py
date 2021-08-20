# 把一些可能其他地方也會用到的function集中
from youtube.settings import DOWNLOADS_DIR, CAPTIONS_DIR, VIDEOS_DIR
import os
from youtube.model.yt import yt


class Utils:
    def __init__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_exist(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def caption_file_exists(self, yt):
        path = yt.captionFilepath
        return os.path.exists(path) and os.path.getsize(path) > 0

    def video_file_exists(self, yt):
        path = yt.videoFilepath
        return os.path.exists(path) and os.path.getsize(path) > 0
