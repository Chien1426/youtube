from youtube.pipeline.steps.get_video_list import GetVideoList
from youtube.pipeline.steps.dowmload_captions import DownloadCaptions
from youtube.pipeline.pipeline import Pipeline
from youtube.utils import Utils
from youtube.pipeline.steps.preflight import Preflight
from youtube.pipeline.steps.postflight import Postflight

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


# 通常我們把要執行的程式寫在main.py
def main():
    inputs = {
        'channel_id': CHANNEL_ID,
    }
    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
