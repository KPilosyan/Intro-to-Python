import pretty_print

def calculate_cube(x):
    return x**3

def calculate_square(x):
    return x**2

def main():
    a = calculate_square(2)
    b = calculate_cube(4)
    pretty_print.simple_print(a)
    pretty_print.pro_print(b)

main()