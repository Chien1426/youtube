from .steps import Step
from moviepy.editor import VideoFileClip, concatenate_videoclips


class EditVideo(Step):
    def process(self, transporter, inputs, utils):
        if utils.edit_videos_file_exists(inputs):
            print('影片已編輯完成')
            return
        print('影片開始製作')
        n = 1
        clips = []
        for found in transporter:
            start = found.time_start
            end = round(found.time_end, 3)
            print('第', n, '支影片加入剪輯區')
            n += 1
            video = VideoFileClip(found.yt.videoFilepath).subclip(start, end)
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break
        print('開始剪輯')
        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile(utils.get_output_filename(inputs['channel_id'], inputs['search_word']))
        print('剪輯結束')