import pytest
import intervaltree.intervaltree
from collections import namedtuple


class TestClass:
    filter = 0


def test_that_filter_dont_break_nuthin():
    it = intervaltree.intervaltree.IntervalTree()
    testResource = TestClass()
    testResource.value='available'
    it[3:8] = testResource
    x = it[5]

    element = x.pop()
    assert element.data == testResource


def test_that_filter_does_something():
    it = intervaltree.intervaltree.IntervalTree()
    testResource = TestClass()
    testResource.value = 'available'

    testResource2 = TestClass()
    testResource2.value = 'unavailable'
    testResource2.filter = 1

    it[3:8] = testResource
    it[3:8] = testResource2

    x = it.search(5, filter=0)
    assert len(x) == 1
    element = x.pop()
    assert element.data == testResource
    

if __name__ in ("__main__", 'test.filtered_tree_tests.filtered_tree_node') :
    pytest.main([__file__, '-v'])
