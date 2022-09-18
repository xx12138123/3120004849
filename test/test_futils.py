import pytest
import futils


def test_read():
    assert len(futils.read_text("../text/orig.txt")) == 10511


if __name__ == "__main__":
    pytest.main('-q test_futils.py')
