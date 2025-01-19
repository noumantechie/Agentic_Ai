from hello_world import main


def test_function1():
    res = main.first_function()
    assert res == "Hello World"


def test_function2():
    res = main.first_function()
    assert res != "Pakistan"
