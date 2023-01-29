import time

import hashlib


class Block:

    def __init__(self, data, prev, index):
        self.index = index
        self.nonce = 0
        self.timestamp = int(time.time())
        self.prev = prev
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        difficulty = 4

        self.hash = ''

        nonce = 0

        target = '0000'

        while self.hash[0:difficulty] != target:
            block = self.prev + str(self.timestamp) + str(nonce) + str(self.data) + str(self.index)
            block = block.encode('utf-8')
            self.hash = (hashlib.sha256(block).hexdigest())
            nonce+=1

        self.nonce = nonce
        print('#' +str(self.index)+ ' block mining completed ....')
        return self.hash
