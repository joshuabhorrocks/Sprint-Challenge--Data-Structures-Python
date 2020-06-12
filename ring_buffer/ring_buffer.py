import collections

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def append(self, item):
        if len(self.buffer) == self.capacity:
            self.buffer.pop(0)
        self.buffer.append(item)


    def get(self):
        return self.buffer