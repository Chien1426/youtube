from .steps import Step
import json



class ReadCaptions(Step):
    def process(self, data, inputs, utils):
        print('處理字幕中......')
        captionArray = []
        # {'text': "reality-show girlfriend Francesca she's", 'start': 406.419, 'duration': 5.161}
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue
            try:
                with open(yt.captionFilepath, 'r', encoding='utf-8') as f:
                    for line in f:
                        captionDict = eval(line)
                        captionArray.append(captionDict)
                        yt.captions = captionArray
                    # yt.captions = mew.split(',')[0]
            except UnicodeDecodeError:
                # print('utf-8 codec cant decode', yt.id)
                continue
        return data
