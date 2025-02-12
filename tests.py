import reminder as app
from reminder import Task
import datetime as dt
import pytest



def test_to_date():
    assert app._to_date('2022-09-02') == dt.date(2022, 9, 2)


def test_to_date_exception():
    with pytest.raises(ValueError):
        app._to_date('1132')

@pytest.fixture
def task_list():
    return [Task(name='pay rent'), Task(name='buy bread')]

# this test will be like both of the following tests 
#the test with multiple parameter with pytest
@pytest.mark.parametrize('test_input, expected',
                         [
                             ('buy bread', Task(name='buy bread')),
                             ('buy milk', None)
                         ])
def test_find_task(test_input, expected, task_list):
    # task_list = [Task(name='pay rent'), Task(name='buy bread')]
    assert app._find_task(test_input, task_list) == expected

# def test_find_task():
#     task_list = [Task(name='pay rent'), Task(name='buy bread')]
#     assert app._find_task('buy bread', task_list) == Task(name='buy bread')


# def test_find_none():
#     task_list = [Task(name='pay rent'), Task(name='buy bread')]
#     assert app._find_task('buy milk', task_list) is None

#function name must start with test_
def test_save_load_task_list(task_list):
    app._save_task_list(task_list)
    load_list = app._get_task_list()
    assert task_list == load_list