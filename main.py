import futils
import sys
import cmp_utils


article_a_path = "text/orig.txt"
article_b_path = "text/orig_0.8_del.txt"
out_path = "test.txt"


def set_arg():
    if len(sys.argv) != 4:
        print('参数个数错误，使用方法为：\nPython: python main.py [原文文件] [抄袭版论文的文件] [答案文件]')
    else:
        global article_a_path, article_b_path, out_path
        article_a_path = sys.argv[1]
        article_b_path = sys.argv[2]
        out_path = sys.argv[3]


if __name__ == "__main__":
    if True:
        try:
            article_a = futils.read_text(article_a_path)
            article_b = futils.read_text(article_b_path)
            result = cmp_utils.compare_article(article_a, article_b)
            futils.write_text(out_path, "%.2f" % result)
        except FileNotFoundError as err:
            print("文件不存在或路径出错")
            print(err)
        except Exception as err:
            print("出现异常")
            print(err)
