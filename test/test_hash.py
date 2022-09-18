import pytest
import cmp_utils


def get_word_hash(word):
    return cmp_utils.get_word_hash(word)


# 16位的hash特征
def test_word_hash():
    assert get_word_hash("早晨") == b'8)\xba\x81\x90\xe9\xb2Rf\x08\x9f3I\xb2H\x8f'


if __name__ == "__main__":
    pytest.main('-q test_hash.py')
