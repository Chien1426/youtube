import os
import time
import pickle
from pytube import YouTube
from .steps import Step, StepException
from youtube.settings import CAPTIONS_DIR
from youtube_transcript_api import YouTubeTranscriptApi
from youtube.model.yt import yt


class DownloadCaptions(Step):

    def process(self, data, inputs, utils):
        start = time.time()

        for yt in data:
            print('downloading caption for', yt.id)
            if utils.caption_file_exists(yt):
                print('found existing caption file')
                continue

            try:
                video_id = yt.id
                captions = YouTubeTranscriptApi.get_transcript(video_id)
            except:
                print('非英文或無字幕，網址: ', video_id)
                continue

            with open(yt.get_caption_filepath(), 'wb', ) as f:
                pickle.dump(captions, f)
        end = time.time()
        print('took', end - start, 'seconds')

        return data
