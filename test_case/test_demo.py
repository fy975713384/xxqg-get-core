# -*- coding: utf-8 -*-
import pytest


class C:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(C, cls).__new__(cls)
        return cls.instance


class C123(C):
    pass


class CA(C123):
    def __init__(self):
        self.sign = 'a'
        print(self.sign)


class CB(C123):
    def __init__(self):
        super(CB, self).__init__()
        self.sign = 'b'
        print(self.sign)


class CC:

    def go_to_ca(self):
        return CA()

    def go_to_cb(self):
        return CB()


@pytest.mark.parametrize('t', [1, 2])
def test(t):
    a = CC().go_to_ca() if t == 1 else CC().go_to_cb()
    print(a)


def test_demo():
    assert 0 == 1


@pytest.fixture
def make_customer_record():

    def _make_customer_record(name):
        return {
            "name": name,
            "orders": []
        }

    return _make_customer_record


def test_customer_records(make_customer_record):
    print(make_customer_record("Lisa"))
    print(make_customer_record("Mike"))
    print(make_customer_record("Meredith"))
