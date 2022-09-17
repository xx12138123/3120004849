# 读取文本，自动尝试utf8和gbk编码
def read_text(path):
    try:
        f = open(path, 'r', encoding='utf8')
        text = f.read()
        f.close()
    except UnicodeDecodeError as err:
        f = open(path, 'r', encoding='gbk')
        text = f.read()
        f.close()
    return text


# 写入文件
def write_text(path, content):
    f = open(path, 'w', encoding='utf8')
    f.write(content)
    f.close()
