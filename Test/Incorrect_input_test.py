import unittest
from Incorrect_input import signs_are_correct, smbls_are_correct, brackets_are_correct, input_is_correct
from Rpn import get_list_of_operations_and_operands


class IncorrectSignsTest(unittest.TestCase):
    def test_signs_are_correct_case1(self):
        inp = get_list_of_operations_and_operands('4arccos(3x+3)')
        self.assertEqual(signs_are_correct(inp), [True, 0])

    def test_signs_are_correct_case2(self):
        inp = get_list_of_operations_and_operands('4arccos(3x++3)')
        self.assertEqual(signs_are_correct(inp), [False, 6])

    def test_signs_are_correct_case3(self):
        inp = get_list_of_operations_and_operands('4arccos(3x+3)^+')
        self.assertEqual(signs_are_correct(inp), [False, 9])

    def test_signs_are_correct_case4(self):
        inp = get_list_of_operations_and_operands('4arccos)(3x+3)')
        self.assertEqual(signs_are_correct(inp), [False, 2])

    def test_signs_are_correct_case5(self):
        inp = get_list_of_operations_and_operands('4+arccos(3x+3)+(9)+')
        self.assertEqual(signs_are_correct(inp), [False, 13])

    def test_signs_are_correct_case6(self):
        inp = get_list_of_operations_and_operands('4+arccos(3x+3)+(9)+')
        self.assertEqual(signs_are_correct(inp), [False, 13])

    def test_brackets_are_correct_case1(self):
        inp = get_list_of_operations_and_operands('log(e))(5x^2)')
        self.assertEqual(brackets_are_correct(inp), [False, 4])


class IncorrectBracketsTest(unittest.TestCase):
    def test_brackets_are_correct_case1(self):
        inp = get_list_of_operations_and_operands('log(e))(5x^2)')
        self.assertEqual(brackets_are_correct(inp), [False, 4])

    def test_brackets_are_correct_case2(self):
        inp = get_list_of_operations_and_operands('(log(e)(5x^2)')
        self.assertEqual(brackets_are_correct(inp), [False, 0])

    def test_brackets_are_correct_case3(self):
        inp = get_list_of_operations_and_operands('log(e)(5x^2)')
        self.assertEqual(brackets_are_correct(inp), [True, 0])


class IncorrectSmblsTest(unittest.TestCase):
    def test_smbls_are_correct_case1(self):
        inp = get_list_of_operations_and_operands('(()log(e)(5x^2)')
        self.assertEqual(smbls_are_correct(inp), [True, 0])

    def test_smbls_are_correct_case2(self):
        inp = get_list_of_operations_and_operands('reglog(e)(5x^2)')
        self.assertEqual(smbls_are_correct(inp), [False, 0])

    def test_smbls_are_correct_case3(self):
        inp = get_list_of_operations_and_operands('log?:(5x^2)')
        self.assertEqual(smbls_are_correct(inp), [False, 1])


class IncorrectInputTest(unittest.TestCase):
    def test_input_is_correct_case1(self):
        inp = get_list_of_operations_and_operands('()log(e)(5x^2)')
        self.assertEqual(input_is_correct(inp), [False, 1])

    def test_input_is_correct_case2(self):
        inp = get_list_of_operations_and_operands('+log(e)(5x^2)')
        self.assertEqual(input_is_correct(inp), [False, 0])

    def test_input_is_correct_case3(self):
        inp = get_list_of_operations_and_operands('log(ei)((5x^2)')
        self.assertEqual(input_is_correct(inp), [False, 2])

    def test_input_is_correct_case4(self):
        inp = get_list_of_operations_and_operands('(18sin(3x^5))/98ln(45x)')
        self.assertEqual(input_is_correct(inp), [True, 0])
