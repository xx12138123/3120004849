import futils
import sys
import cmp_utils


article_a_path = "text/orig.txt"
article_b_path = "text/orig_0.8_del.txt"
out_path = "test.txt"


def set_arg():
    if len(sys.argv) != 4:
        print('参数个数错误，使用方法为：\nPython: python main.py [原文文件] [抄袭版论文的文件] [答案文件]')
        return False
    else:
        global article_a_path, article_b_path, out_path
        article_a_path = sys.argv[1]
        article_b_path = sys.argv[2]
        out_path = sys.argv[3]
        return True


if __name__ == "__main__":
    if set_arg():
        try:
            article_a = futils.read_text(article_a_path)
            article_b = futils.read_text(article_b_path)
            if len(article_a) < 200 or len(article_b) < 200:
                print("文章太短，字数应在两百以上")
            else:
                cmp_utils.initialize()
                result = cmp_utils.compare_article(article_a, article_b)
                if result < 0:
                    print("文章非中文，分词数量较少")
                else:
                    futils.write_text(out_path, "%.2f" % result)
        except FileNotFoundError as err:
            print("文件不存在或路径出错")
            print(err)
        except Exception as err:
            print("出现异常")
            print(err)
