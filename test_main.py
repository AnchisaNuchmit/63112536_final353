from main import buything, buying
import pytest

@pytest.mark.code # pytest -m code
def test_input1():
    type = 1
    excepted_result = "Espresso"
    actual_result = buything(type)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_input2():
    type = 2
    excepted_result = "Cappuccino"
    actual_result = buything(type)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_input3():
    type = 3
    excepted_result = "Latte"
    actual_result = buything(type)
    assert excepted_result == actual_result

@pytest.mark.code # pytest -m code
def test_input4():
    type = 4
    excepted_result = "Mocha"
    actual_result = buything(type)
    assert excepted_result == actual_result