import unittest
from app import calculate_area

class TestApp(unittest.TestCase):
    
    def test_area_calculation(self):
        # בדיקה ששטח של 5X2 הוא אכן 10
        self.assertEqual(calculate_area(5, 2), 10)

    def test_area_zero(self):
        # בדיקה ששטח עם אפס הוא אפס
        self.assertEqual(calculate_area(0, 10), 0)

if __name__ == '__main__':
    unittest.main()
