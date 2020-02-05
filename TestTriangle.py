# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3, 4, 5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5, 3, 4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1, 1, 1 should be equilateral')

    def testIsoscelesTrianglesA(self):
        self.assertEqual(classifyTriangle(3, 3, 4), 'Isosceles', '3, 3, 4 should be isosceles')

    def testIsoscelesTrianglesB(self):
        self.assertEqual(classifyTriangle(3, 4, 3), 'Isosceles', '3, 4, 3 should be isosceles')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(5, 6, 7), 'Scalene', '5, 6, 7 should be Scalene')

    def testWrongTrianglesA(self):
        self.assertEqual(classifyTriangle(300, 300, 300), 'InvalidInput', '300, 300, 300 are invalid input')

    def testWrongTrianglesB(self):
        self.assertEqual(classifyTriangle(-3, -4, -5), 'InvalidInput', '-3, -4, -5 are invalid input')

    def testWrongTrianglesC(self):
        self.assertEqual(classifyTriangle('a', ('b',), ['c']), 'InvalidInput', "'a', ('b',), ['c'] are invalid input")

    def testWrongTrianglesD(self):
        self.assertEqual(classifyTriangle(3, 3, 6), 'NotATriangle', '3, 3, 6 is not a triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
