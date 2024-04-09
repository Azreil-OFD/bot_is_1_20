import unittest
from services import get_random, get_pong

class TestYourScript(unittest.TestCase):

    # Тесты для функции get_random

    def test_get_random_within_range(self):
        result = get_random(1, 6)
        self.assertTrue(1 <= result <= 6)

    def test_get_random_default_range(self):
        result = get_random()
        self.assertTrue(1 <= result <= 6)

    def test_get_random_custom_range(self):
        result = get_random(10, 15)
        self.assertTrue(10 <= result <= 15)

    def test_get_random_invalid_range(self):
        with self.assertRaises(ValueError):
            get_random(6, 1)

    # Тест для функции get_pong

    def test_get_pong_output(self):
        result = get_pong()
        self.assertEqual(result, "pong")

if __name__ == '__main__':
    unittest.main()
