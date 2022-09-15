import cv2
import numpy

def read_text(path):
    f = open(path, 'r')
    text = f.read()
    f.close()
    return text


def write_text(path, content):
    f = open(path, 'w')
    f.write(content)
    f.close()




split_size = 128
