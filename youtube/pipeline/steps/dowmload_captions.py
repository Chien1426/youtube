import os
import time
import pickle
from pytube import YouTube
from .steps import Step, StepException
from youtube.settings import CAPTIONS_DIR
from youtube_transcript_api import YouTubeTranscriptApi


class DownloadCaptions(Step):

    def process(self, data, inputs, utils):
        start = time.time()

        for url in data:
            print('downloading caption for', url)
            if utils.caption_file_exists(url):
                print('found existing caption file')
                continue

            try:
                video_id = utils.get_video_id(url)
                captions = YouTubeTranscriptApi.get_transcript(video_id)
            except:
                print('非英文或無字幕，網址: ', video_id)
                continue

            with open(utils.get_caption_filepath(url), 'wb', ) as f:
                pickle.dump(captions, f)
        end = time.time()
        print('took', end - start, 'seconds')

        return data
