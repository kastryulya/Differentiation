import unittest
import main


class DifferentiationTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(main.process('ln(2x-4)'), '(2/((2*x)-4))')

    def test_case2(self):
        self.assertEqual(main.process('x^3/(5*x)+10'), '((((3*(x^2))*(5*x))-((x^3)*5))/((5*x)^2))')

    def test_case3(self):
        self.assertEqual(main.process('3ln(x)* cos(tg(x))'),
                         '(((3*(1/x))*(cos(tgx)))+((3*(lnx))*((-1*(1/((cosx)^2)))*(sin(tgx)))))')

    def test_case4(self):
        self.assertEqual(main.process('arcsin(5+ sin(43))'), '0')

    def test_case5(self):
        self.assertEqual(main.process('log(e)(5x^2)'), '((5*(2*x))/(5*(x^2)))')

    def test_case6(self):
        self.assertEqual(main.process('e^(2x)'), '((e^(2*x))*2)')

    def test_case7(self):
        self.assertEqual(main.process('arccos(3x+2)'), '(-3/((1-(((3*x)+2)^2))^0.5))')

    def test_case8(self):
        self.assertEqual(main.process('ctg(x(2x+4))'), '((0-(((2*x)+4)+(x*2)))/((sin(x*((2*x)+4)))^2))')

    def test_case9(self):
        self.assertEqual(main.process('arcctg((2x+34)x)'), '((-1*((2*x)+((2*x)+34)))/(1+((((2*x)+34)*x)^2)))')

    def test_case10(self):
        self.assertEqual(main.process('arctg((2x+34)x)'), '(((2*x)+((2*x)+34))/(1+((((2*x)+34)*x)^2)))')

    def test_case11(self):
        self.assertEqual(main.process('(3^2)x'), '9')

    def test_case12(self):
        self.assertEqual(main.process('sin(log(2)(4x))'), '((4/((4*x)*(loge2)))*(cos(log2(4*x))))')

    def test_case13(self):
        self.assertEqual(main.process('sin(ln(4x)*ln(e))'), '((4/(4*x))*(cos(ln(4*x))))')

    def test_case14(self):
        self.assertEqual(main.process('sinln(4x)*ln(e))'), 'Input is wrong! Position error: 0.')

    def test_case15(self):
        self.assertEqual(main.process('e^(2x)f*'), 'Input is wrong! Position error: 6.')
