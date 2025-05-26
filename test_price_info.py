import price_info

print("Test price_infp.py")

def test_cost_of_fruits():
    result = 0
    fruit = 'apple'
    quantity = 5
    result = price_info.price_list[fruit]*quantity
    assert (result == 6.0)


def test_cost_shopping():

    result = price_info.total_cost_shopping()
    expected_result = 46.75
    assert (result == expected_result)
    