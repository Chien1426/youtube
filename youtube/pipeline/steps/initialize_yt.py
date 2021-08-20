from .steps import Step
from youtube.model.yt import yt


class InitializeYT(Step):
    def process(self, data, inputs, utils):
        return [yt(url) for url in data]
