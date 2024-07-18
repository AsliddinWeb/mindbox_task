import math
import unittest

from shape_library import Circle, Triangle, get_area

class TestShapeLibrary(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.get_area(), math.pi * 25, places=10)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.get_area(), 6, places=10)

    def test_is_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_get_area(self):
        circle = Circle(5)
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(get_area(circle), math.pi * 25, places=10)
        self.assertAlmostEqual(get_area(triangle), 6, places=10)

if __name__ == '__main__':
    unittest.main()
