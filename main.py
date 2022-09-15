import cv2
import numpy

def read_text(path):
    f = open(path, 'r', encoding='utf8')
    text = f.read()
    f.close()
    return text


def write_text(path, content):
    f = open(path, 'w', encoding='utf8')
    f.write(content)
    f.close()


def get_features(text):
    p = []
    split_size = int(len(text) / split_num)
    for i in range(split_num):
        split_text = text[i * split_size:(i + 1) * split_size]
        num = 0
        for c in split_text:
            num += ord(c)
        p.append(int(num / split_size))

    p.sort(reverse=True)
    return p


split_num = 128
f_a = get_features(read_text("text/orig.txt"))
f_b = get_features(read_text("text/orig_0.8_dis_1.txt"))

result = 0
for i in range(split_num):
    result += abs(f_a[i] - f_b[i])

print(result)
print(1 - (result/(split_num * 1024)))
