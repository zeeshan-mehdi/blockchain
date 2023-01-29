# This is a sample Python script.
import json

from block import Block
from student import Student

from Crypto.Cipher import AES


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def addBlock(blocks, newBlock, prev, index):
    block = Block(newBlock,prev,index)
    blocks.append(block)
    print('block added : ', block.__dict__)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    key = 'this is password'
    blocks = []

    aes = AES.new(key.encode(), AES.MODE_CBC)

    student = Student('Zeeshan Mehdi', 'SE')

    studentJson = json.dumps(student.__dict__)

    pad = b' '

    plain_text = studentJson.encode()

    length = 16 - (len(studentJson) % 16)

    plain_text += length * pad

    cipher = aes.encrypt(plain_text)

    addBlock(blocks, cipher, '0', len(blocks))


    student = Student('Mushtaq', 'OEX')

    studentJson = json.dumps(student.__dict__)


    plain_text = studentJson.encode()

    length = 16 - (len(studentJson) % 16)

    plain_text += length * pad

    cipher = aes.encrypt(plain_text)

    addBlock(blocks, cipher, blocks[len(blocks)-1].hash, len(blocks))
