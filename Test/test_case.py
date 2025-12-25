# import unittest
# from calc import divide
# from utils import is_even, greet

# # class TestIsIven(unittest.TestCase):
    
# #     # Каждый тест - это def с именем "test_"

# #     def test_even_numbers(self): 
# #         # Тут хочу получать четные числа = True
# #         self.assertTrue(is_even(2)) # is_even(2) == True, OK
# #         self.assertTrue(is_even(0))
# #         self.assertTrue(is_even(-4))
    
# #     def test_odd_numbers(self): 
# #         # Тут хочу получать четные числа = False
# #         self.assertFalse(is_even(1)) #  is_even(2) == False, OK
# #         self.assertFalse(is_even(7))
# #         self.assertFalse(is_even(-3))

# class TestGreet(unittest.TestCase):

#     def test_normal_case(self):
#         self.assertEqual(greet('Anna'), 'Привет, Anna')

#     def test_for_Evg(self):

#         with self.assertRaises(TypeError):
#             divide("пять", 2)

#         with self.assertRaises(TypeError):
#             divide(None, 2)

#         with self.assertRaises(ZeroDivisionError):
#             divide(10, 0)
# if __name__ == '__main__':
#     unittest.main()

import unittest
from calc import divide
from utils import is_even, greet

class TestAssert(unittest.TestCase):

    def test_equal(self):
        """
        a == b?
        """
        a = 5
        b = 5
        self.assertEqual(a, b)  # a == b, OK, иначе - error
    
    def test_not_equal(self):
        """
        a == b?
        """
        a = 5
        b = 3
        self.assertNotEqual(a, b)  # a != b, OK, иначе - error

    def test_true(self):
        x = True
        self.assertTrue(x) # x == true

    def test_false(self):
        x = False
        self.assertFalse(x) # x == False

    def test_is(self):
        a = [1, 2]
        b = a
        self.assertIs(a, b) # x == False

if __name__ == '__main__':
    unittest.main()