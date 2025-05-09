import price_info

print("Test price_infp.py")

def test_cost_of_fruits():
    result = 0
    fruit = 'apple'
    quantity = 5
    result = price_info.price_list[fruit]*quantity
    assert (result == 6.0)


def test_cost_of_fruits_():
    result = 0
    fruit = 'apple'
    quantity = 10
    result = price_info.price_list[fruit]*quantity
    assert (result == 12.0)
    