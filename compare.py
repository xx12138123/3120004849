import jieba
import os
import hashlib

SPLIT_SIZE = 128

#结巴分词会在系统cache写入模型文件，故手动初始化
def initialize(self=jieba.dt):
    abs_path = self.dictionary
    with self.lock:
        try:
            with jieba.DICT_WRITING[abs_path]:
                pass
        except KeyError:
            pass
        if self.initialized:
            return
        cache_file = "dict\\jieba.cache"
        if os.path.isfile(cache_file) and (abs_path == jieba.DEFAULT_DICT or
                                           os.path.getmtime(cache_file) > os.path.getmtime(abs_path)):
            try:
                with open(cache_file, 'rb') as cf:
                    self.FREQ, self.total = jieba.marshal.load(cf)
                load_from_cache_fail = False
            except Exception:
                load_from_cache_fail = True
        self.initialized = True



#分词后获取词频
def get_word_frequency(article):
    #初始化检测
    if not jieba.dt.initialized:
        initialize()
    #调用引擎分词
    seg_list = jieba.cut(article)

    #计算词频
    counts = {}
    for word in seg_list:
        if len(word) == 1:
            continue
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    #排序（返回由元组组成的列表，如[('家珍', 32), ('自己', 27)]）
    items.sort(key=lambda x: x[1], reverse=True)
    return items



def get_word_hash(word):
    return hashlib.md5(word.encode(encoding="utf8")).digest()


def get_article_hash(article):
    seg_list = get_word_frequency(article)
    #计算所有分词次数总和
    k_sum = 0
    for i in seg_list:
        k_sum += i[1]
    #计算hash
    hash_result = [0] * SPLIT_SIZE
    for i in seg_list:
        hash_bytes = get_word_hash(i[0])
        k = (10 * i[1] / k_sum)
        for bi in range(SPLIT_SIZE):
            #循环取位，然后判断是否为0
            r = hash_bytes[bi >> 3] & (0x80 >> (bi % 8))
            if r == 0:
                hash_result[bi] -= k
            else:
                hash_result[bi] += k
        ''' 旧算法，不直观
        for bi in range(len(hash_bytes)):
            for ji in range(8):
                r = hash_bytes[bi] & (0x01 << ji)
                if r == 0:
                    hash_result[bi*8+7-ji] -= k
                else:
                    hash_result[bi * 8 + 7 - ji] += k'''
    #返回真值列表
    return [hash_result[i] > 0 for i in range(len(hash_result))]





def compare_article(article_a, article_b):
    article_a_hash = get_article_hash(article_a)
    article_b_hash = get_article_hash(article_b)
    distance = 0
    for i in range(SPLIT_SIZE):
        if article_a_hash[i] != article_b_hash[i]:
            distance += 1
    return 0.01 * (100 - distance * 100 / SPLIT_SIZE)
