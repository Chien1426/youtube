# 結束清理資料
from .steps import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        print('後製作業開始，準備結束程式。')
        pass
