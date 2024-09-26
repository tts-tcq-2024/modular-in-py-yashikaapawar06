MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def get_color_pairs():
    total_pairs = len(MAJOR_COLORS) * len(MINOR_COLORS)
    return [(i + 1, MAJOR_COLORS[i // len(MINOR_COLORS)], MINOR_COLORS[i % len(MINOR_COLORS)]) for i in range(total_pairs)]

def format_color_pair(pair_number, major_color, minor_color):
    return f'{pair_number}: {major_color} {minor_color}'

def print_reference_manual():
    color_pairs = get_color_pairs()
    for pair in color_pairs:
        print(format_color_pair(*pair))

if __name__ == '__main__':
    print_reference_manual()
