# def test_a():
#     print("Inside method A")

# def test_b():
#     print("Inside method B")

# def test_c():
#     print("Inside method C")

import allure


@allure.feature("Feature1")
@allure.story("Story1")
def test_minor():
    assert False


@allure.feature("Feature2")
@allure.story("Story2", "Story3")
@allure.story("Story4")
class TestBar:

    # will have 'Feature2 and Story2 and Story3 and Story4'
    def test_bar(self):
        pass
