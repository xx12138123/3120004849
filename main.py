import futils
import os
import sys
import compare


def set_arg():
    result = False
    if len(sys.argv) != 4:
        print('参数个数错误，使用方法为：\n')
    else:
        result &= os.path.exists(sys.argv[1])
        result &= os.path.isfile(sys.argv[1])
        result &= os.path.exists(sys.argv[1])
        result &= os.path.isfile(sys.argv[1])


article_a = futils.read_text("text//orig.txt")
article_b = futils.read_text("text//orig_0.8_dis_1.txt")


print(compare.compare_article(article_a, article_b))
