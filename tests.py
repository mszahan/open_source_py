import reminder as app
from reminder import Task
import pytest



# this test will be like both of the following tests 
#the test with multiple parameter with pytest
@pytest.mark.parametrize('test_input, expected',
                         [
                             ('buy bread', Task(name='buy bread')),
                             ('buy milk', None)
                         ])
def test_find_task(test_input, expected):
    task_list = [Task(name='pay rent'), Task(name='buy bread')]
    assert app._find_task(test_input, task_list) == expected

# def test_find_task():
#     task_list = [Task(name='pay rent'), Task(name='buy bread')]
#     assert app._find_task('buy bread', task_list) == Task(name='buy bread')


# def test_find_none():
#     task_list = [Task(name='pay rent'), Task(name='buy bread')]
#     assert app._find_task('buy milk', task_list) is None
