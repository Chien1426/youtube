# 結束清理資料
from .steps import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        print('in Postflight')
