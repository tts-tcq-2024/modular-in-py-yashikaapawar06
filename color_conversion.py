from color_coding import MAJOR_COLORS, MINOR_COLORS

def validate_color_index(index, color_list):
    return 0 <= index < len(color_list)

def get_color_from_pair_number(pair_number):
    major_index, minor_index = divmod(pair_number - 1, len(MINOR_COLORS))
    if not validate_color_index(major_index, MAJOR_COLORS):
        raise ValueError('Invalid pair number')
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def get_pair_number_from_color(major_color, minor_color):
    if major_color not in MAJOR_COLORS or minor_color not in MINOR_COLORS:
        raise ValueError('Invalid color input')
    major_index = MAJOR_COLORS.index(major_color)
    minor_index = MINOR_COLORS.index(minor_color)
    return major_index * len(MINOR_COLORS) + minor_index + 1
