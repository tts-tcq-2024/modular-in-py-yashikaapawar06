from color_conversion import get_color_from_pair_number, get_pair_number_from_color

def test_number_to_pair(pair_number, expected_major, expected_minor):
    major, minor = get_color_from_pair_number(pair_number)
    assert (major, minor) == (expected_major, expected_minor), f"Failed: {pair_number}"

def test_pair_to_number(major_color, minor_color, expected_number):
    pair_number = get_pair_number_from_color(major_color, minor_color)
    assert pair_number == expected_number, f"Failed: {major_color}, {minor_color}"

if __name__ == '__main__':
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    print('All tests passed!')
