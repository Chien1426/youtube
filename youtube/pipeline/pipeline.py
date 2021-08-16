from .steps.steps import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None
        for step in self.steps:
            print(step)
            try:
                data = step.process(data, inputs, utils)  # data為每一個Step加工完後產生的東西
            except StepException as e:
                print('Exception happen:', e)
                break
