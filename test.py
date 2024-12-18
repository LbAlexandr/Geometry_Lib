import unittest
import math

from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter

class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle_area(5, 10), 50)
        self.assertEqual(rectangle_area(500, 123), 61500)
        self.assertEqual(rectangle_area(1, 1), 1)
        self.assertEqual(rectangle_area(5, 0), 0)
        self.assertEqual(rectangle_area(5, 5), 25)
        self.assertEqual(rectangle_area(-1, 1), -1)
        self.assertEqual(rectangle_area(-12, -12), 144)
        self.assertEqual(rectangle_area(0, 0), 0)
        self.assertEqual(rectangle_area(10000000000, 10000000000), 100000000000000000000)
        self.assertEqual(rectangle_area(12 + 15, 30), rectangle_area(12, 30) + rectangle_area(15, 30))
        self.assertEqual(rectangle_area(12, 30), rectangle_area(30, 12))
    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter(5, 10), 30)
        self.assertEqual(rectangle_perimeter(1, 1), 4)
        self.assertEqual(rectangle_perimeter(-12, -10), -44)
        self.assertEqual(rectangle_perimeter(5, -10), -10)
        self.assertEqual(rectangle_perimeter(0, 0), 0)
        self.assertEqual(rectangle_perimeter(10000000000000, 10000000000000), 40000000000000)
        self.assertEqual(rectangle_perimeter(300, 400), rectangle_perimeter(400, 300))

class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(5), 25)
        self.assertEqual(square_area(500), 250000)
        self.assertEqual(square_area(1), 1)
        self.assertEqual(square_area(0), 0)
        self.assertEqual(square_area(5), 25)
        self.assertEqual(square_area(-1), 1)
        self.assertEqual(square_area(-12), 144)
        self.assertEqual(square_area(10000000000), 100000000000000000000)
        self.assertEqual(square_area(12 + 15), 12 * 12 + 2 * 12 * 15 + 15 * 15)
    def test_perimeter(self):
        self.assertEqual(square_perimeter(5), 20)
        self.assertEqual(square_perimeter(1), 4)
        self.assertEqual(square_perimeter(12), 48)
        self.assertEqual(square_perimeter(-10), -40)
        self.assertEqual(square_perimeter(0), 0)
        self.assertEqual(square_perimeter(10000000000000), 40000000000000)

class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle_area(5, 10), 25)
        self.assertEqual(triangle_area(500, 123), 61500/2)
        self.assertEqual(triangle_area(1, 1), 1/2)
        self.assertEqual(triangle_area(5, 0), 0)
        self.assertEqual(triangle_area(5, 5), 25/2)
        self.assertEqual(triangle_area(-1, 1), -1/2)
        self.assertEqual(triangle_area(-12, -12), 72)
        self.assertEqual(triangle_area(0, 0), 0)
        self.assertEqual(triangle_area(10000000000, 10000000000), 50000000000000000000)
        self.assertEqual(triangle_area(12 + 15, 30), triangle_area(12, 30) + triangle_area(15, 30))
        self.assertEqual(triangle_area(30, 12 + 15), triangle_area(30, 12) + triangle_area(30, 15))
        self.assertEqual(triangle_area(12, 30), triangle_area(30, 12))
    def test_perimeter(self):
        self.assertEqual(triangle_perimeter(5, 10, 15), 30)
        self.assertEqual(triangle_perimeter(1, 1, 1), 3)
        self.assertEqual(triangle_perimeter(-12, -10, 30), 8)
        self.assertEqual(triangle_perimeter(5, -10, 5), 0)
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)
        self.assertEqual(triangle_perimeter(10000000000000, 10000000000000, 10000000000000), 30000000000000)
        self.assertEqual(triangle_perimeter(300, 400, 500), triangle_perimeter(400, 500, 300))
        self.assertEqual(triangle_perimeter(300, 400, 500), triangle_perimeter(300, 500, 400))
        self.assertEqual(triangle_perimeter(300, 400, 500), triangle_perimeter(500, 400, 300))

class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(circle_area(5), 25*math.pi)
        self.assertEqual(circle_area(500), 250000*math.pi)
        self.assertEqual(circle_area(1), math.pi)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(5), 25*math.pi)
        self.assertEqual(circle_area(-1), math.pi)
        self.assertEqual(circle_area(-12), 144*math.pi)
        self.assertEqual(circle_area(10000000000), 100000000000000000000*math.pi)
        self.assertEqual(circle_area(12 + 15), (12 * 12 + 2 * 12 * 15 + 15 * 15)*math.pi)
    def test_perimeter(self):
        self.assertEqual(circle_perimeter(5), 10*math.pi)
        self.assertEqual(circle_perimeter(1), 2*math.pi)
        self.assertEqual(circle_perimeter(12), 24*math.pi)
        self.assertEqual(circle_perimeter(-10), -20*math.pi)
        self.assertEqual(circle_perimeter(0), 0)
        self.assertEqual(circle_perimeter(10000000000000), 20000000000000*math.pi)
        

if __name__ == '__main__':
    unittest.main()
