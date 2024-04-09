import unittest
from services import get_random, get_pong, calculate_expression

class TestBot(unittest.TestCase):
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
    
    # Тест для функции calculate_expression
    def test_calculate_expression(self):
        result = calculate_expression("1 + 2")
        self.assertTrue(result == 3)

    def test_calculate_expression_error(self):
        result = calculate_expression("1 + 2 )")
        self.assertTrue(result == "Ошибка: unmatched ')'")

if __name__ == '__main__':
    unittest.main()
