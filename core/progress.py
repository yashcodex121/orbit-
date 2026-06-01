import time

class ProgressTracker:
    def __init__(self):
        self.start = time.time()

    async def __call__(self, current, total):
        pass
