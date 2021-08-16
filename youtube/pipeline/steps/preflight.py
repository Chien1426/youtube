#一開始先建立資料夾
from .steps import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        print('in Preflight')
        utils.create_dirs()
