import time
import binascii
from slim.utils import ObjectID


def test_my_object_id():
    a = ObjectID()
    b = ObjectID('56222d21293b328eb0000002')
    c = ObjectID('56222d21293b328eb0000002')
    time.sleep(1)
    d = ObjectID()
    e = ObjectID()

    # 明确时间差距
    assert a > b
    assert a >= b
    assert a != b
    assert b < a
    assert b <= a

    # 长度与值
    assert len(a) == 24
    assert len(a.to_bin()) == 12
    assert str(binascii.hexlify(a.to_bin()), 'utf-8') == str(a)

    assert str(b) == '56222d21293b328eb0000002'
    assert b.to_bin() == b'V"-!);2\x8e\xb0\x00\x00\x02'

    # 相等
    assert a != b
    assert b == c
    assert id(b) != id(c)

    # 时间测试，相隔一秒
    assert d > a
    assert d >= a
    assert d != a
    assert a < d
    assert a <= d

    # 时间测试，紧邻创建
    assert e > d
    assert e >= d
    assert e != d
    assert d < e
    assert d <= e

    # 比较类型
    try:
        a < 1
    except Exception as e:
        assert isinstance(e, TypeError)

    try:
        a <= 1
    except Exception as e:
        assert isinstance(e, TypeError)

    try:
        a == 1
    except Exception as e:
        assert isinstance(e, TypeError)

    try:
        a != 1
    except Exception as e:
        assert isinstance(e, TypeError)

    try:
        a > 1
    except Exception as e:
        assert isinstance(e, TypeError)

    try:
        a >= 1
    except Exception as e:
        assert isinstance(e, TypeError)

    # 其他
    assert repr(a).startswith('ObjectID')
    assert ObjectID.check_valid(a.digest())
    assert ObjectID.check_valid(a.hexdigest())


if __name__ == '__main__':
    test_my_object_id()
