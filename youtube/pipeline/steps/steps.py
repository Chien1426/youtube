# 寫不同功能的步驟
from abc import ABC, abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs, utils):  # input為一個參數的陣列,預防可能有些function才需要用到某些參數,就不用一直加上
        pass


class StepException(Exception):
    pass
