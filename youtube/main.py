from youtube.pipeline.steps.get_video_list import GetVideoList
from youtube.pipeline.steps.initialize_yt import InitializeYT
from youtube.pipeline.steps.dowmload_captions import DownloadCaptions
from youtube.pipeline.steps.read_caption import ReadCaptions
from youtube.pipeline.steps.search import Search
from youtube.pipeline.steps.downloadVideo import DownLoadVideos
from youtube.pipeline.steps.editVideo import EditVideo
from youtube.pipeline.pipeline import Pipeline
from youtube.utils import Utils
from youtube.pipeline.steps.preflight import Preflight
from youtube.pipeline.steps.postflight import Postflight

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


# 通常我們把要執行的程式寫在main.py
def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
        'limit' : 5,
    }
    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaptions(),
        Search(),
        DownLoadVideos(),
        EditVideo(),
        Postflight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
