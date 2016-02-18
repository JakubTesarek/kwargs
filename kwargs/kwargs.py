def run(callback, *args, **kwargs):
    return callback(*args, **kwargs)


class App(object):
    def __init__(self, callback):
        self.callback = callback

    def run(self, *args, **kwargs):
        return run(self.callback, *args, **kwargs)