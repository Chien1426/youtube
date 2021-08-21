from youtube.pipeline.steps.steps import Step
from pytube import YouTube
from youtube.settings import VIDEOS_DIR
import os
import urllib.request


class DownLoadVideos(Step):
    def process(self, data, inputs, utils):
        # yt_set = set([found.yt for found in data])
        for found in data:
            yto = found.yt
            url = yto.url
            print('downloading', url)
            if utils.video_file_exists(yto):
                print(f'found existing video file for {url}')
                continue
            try:
                YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yto.id + '.mp4')
            except urllib.error.HTTPError:
                continue
        return data
