def read_text(path):

    f = open(path, 'r', encoding='utf8')
    text = f.read()
    f.close()
    return text


def write_text(path, content):
    f = open(path, 'w', encoding='utf8')
    f.write(content)
    f.close()

