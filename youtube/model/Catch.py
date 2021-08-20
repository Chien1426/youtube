class CatchYTO:
    def __init__(self, yto, time_start, time_duration):
        self.yto = yto
        self.time_start = time_start
        self.time_duration = time_duration
        self.time_end = self.time_ends()

    def time_ends(self):
        return self.time_start + self.time_duration