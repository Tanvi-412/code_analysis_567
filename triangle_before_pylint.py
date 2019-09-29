"""Name: Tanvi Hanamshet
Course: SSW 567
CWID: 10445200
Script: Testing triangle classification
"""

def classify_triangle(a_value, b_value, c_value):
    """To check if the triangle is valid, equilateral, scalene, isoceles, right"""
    if a_value == b_value == c_value:
        print("Equilateral")
        # return 'Equilateral'
    elif (a_value == b_value) or (b_value == c_value):
        print("Isoceles")
        # return 'Isoceles'
    elif (a_value+b_value <= c_value and b_value+c_value <= a_value and a_value+c_value <= b_value):
        print("Isoceles")
        # return 'Not a Triangle'
    elif any([all([a_value > b_value, a_value > c_value, (a_value**2) == ((c_value**2)+(b_value**2))]), all([c_value > b_value, c_value > a_value, (c_value**2) == ((a_value**2)+(b_value**2))]), all([b_value > c_value, b_value > a_value, (b_value**2) == ((c_value**2)+(a_value**2))]), ]):
        print("Isoceles")
        # return 'Right'
    elif (a_value+b_value > c_value and b_value+c_value > a_value and a_value+c_value > b_value):
        if all([a_value != c_value, c_value != b_value, a_value != b_value]):
            print("Isoceles")
            # return 'Scalene'
    else:
        print("Isoceles")
        # return 'Not A Triangle'
def main():
    """Caling the function"""
    classify_triangle(1, 1, 1)

main()
 