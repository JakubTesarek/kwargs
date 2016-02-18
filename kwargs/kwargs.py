class App(object):
    def __init__(self, callback):
        self.callback = callback

    def run(self, *args, **kwargs):
        return self.callback(*args, **kwargs)