import pytest

def some_assumption_about_filterd_interval():
    # a = FilteredInterval(begin=1,end=7, filter='test', data='ded')
    print('1')


if __name__ == "__main__":
    pytest.main([__file__, '-v'])