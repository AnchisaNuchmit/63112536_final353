from functions import buything, discountprice
import pytest

@pytest.mark.code # pytest -m code
def test_input1():
    type = 1
    number = 1
    excepted_result = 55
    actual_result = buything(type, number)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_input2():
    type = 2
    number = 1
    excepted_result = 60
    actual_result = buything(type, number)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_input3():
    type = 3
    number = 1
    excepted_result = 65
    actual_result = buything(type, number)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_input4():
    type = 4
    number = 1
    excepted_result = 70
    actual_result = buything(type, number)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_true55():
    total_ = 55
    number = 1
    answer = "True"
    excepted_result = 50
    actual_result = discountprice(total_, number, answer)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_false55():
    total_ = 55
    number = 1
    answer = "False"
    excepted_result = 55
    actual_result = discountprice(total_, number, answer)
    assert excepted_result == actual_result
