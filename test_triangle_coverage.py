"""Name: Tanvi Hanamshet
Course: SSW 567
CWID: 10445200
Script: Testing triangle classification
"""

import unittest
#this pulls function in from the other file:
from triangle import classify_triangle  
 
class ClassifyTriangleTest(unittest.TestCase):
    """testing function classify_triangle"""
    def test_Equilateral(self):
        self.assertAlmostEqual(classify_triangle(2.1, 2.1, 2.1), 'Equilateral' , '2.1, 2.1, 2.1 is a Equilateral triangle')
        self.assertNotEqual(classify_triangle(2.1, 2, 2.1), 'Equilateral' , '2.1, 2, 2.1 is a Isoceles triangle')
        self.assertEqual(classify_triangle(50,50,50), 'Equilateral' , '50,50,50 is a Equilateral triangle')
    
        
    def test_Isoceles(self):
        self.assertAlmostEqual(classify_triangle(1.1,1.1,2), 'Isoceles',  '1.1,1.1,2 is a Isoceles triangle')
        self.assertEqual(classify_triangle(56,56,30),'Isoceles', '56,56,30 is a Isoceles triangle')
        self.assertEqual(classify_triangle(5,5,8), 'Isoceles', '5,5,8 is a Isoceles triangle')
        self.assertNotEqual(classify_triangle(1,1,1),'Isoceles', '56,56,56 is a Equilateral triangle')


    def test_Scalene(self):
        self.assertEqual(classify_triangle(5,4,6), 'Scalene', '5,4,6 is a Scalene triangle')
        self.assertEqual(classify_triangle(35,10,33),'Scalene','35,10,33 is a Scalene triangle')
        self.assertAlmostEqual(classify_triangle(4.5,6.5,5.6),'Scalene','4.5,6.5,5.6 is a Scalene triangle')
        self.assertNotEqual(classify_triangle(56,56,30),'Scalene','56,56,30 is a Isoceles triangle')

    def test_Right(self):
 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertNotEqual(classify_triangle(20.1,34.2,39.67),'Right','20.1,34.2,39.67 is a Right triangle')
        self.assertNotEqual(classify_triangle(35, 10, 33),'Right','35,10,33 is a Scalene triangle')



    def test_NotTriangle(self):
        self.assertEqual(classify_triangle(5,3,8), 'Not A Triangle')
        self.assertEqual(classify_triangle(5,3,0), 'Not A Triangle')
        self.assertAlmostEqual(classify_triangle(3.4,5.6,9), 'Not A Triangle')
        self.assertNotEqual(classify_triangle(1,1,1), 'Not A Triangle', '1,1,1 is a Equilateral triangle')
 

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)


