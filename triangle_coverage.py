"""Name: Tanvi Hanamshet
Course: SSW 567
CWID: 10445200
Script: Testing triangle classification
"""

def classify_triangle(a, b, c):
    """To check if the triangle is valid, equilateral, scalene, isoceles, right"""
    if a == b == c:
        return 'Equilateral'
    elif (a == b) or (b == c):
        return 'Isoceles'
    elif ( a + b <= c and b + c <= a and a + c <= b ):
        return 'Not A Triangle'
    elif any([
        all([a>b, a>c, (a**2)==((c**2)+(b**2))]),
        all([c>b, c>a, (c**2)==((a**2)+(b**2))]),
        all([b>c, b>a, (b**2)==((c**2)+(a**2))]),
        ]):
        return 'Right'
    elif ( a + b > c and b + c > a and a + c > b ):
        if all([a!=c, c!=b, a!=b]):
            return 'Scalene'
    else:
        return 'Not A Triangle'
        
    
        

    