import argparse

from Differentiation import diff, simplify_expr, set_var
from Rpn import opn, from_opn
from Incorrect_input import input_is_correct


def process(inp, order=1, var='x'):
    # input validation
    inp_is_corr = input_is_correct(inp)
    if not inp_is_corr[0]:
        return f'''Input is wrong! Position error: {inp_is_corr[1]}.
        
The logarithm is written as log(2)(3x), where (2) is the base 
(mandatory in brackets), (3x) is the argument. 
Multiplication signs can miss only between numeric factors 
and expression/variable/brackets. Wrong: (56xy/(12x-1))(2xsin(y)+4). 
Correct: (56x*y/(12x-1))*(2x*sin(y)+4). 
Negative numbers are entered in the form (0-3).'''

    temp_expr = inp

    for i in range(order):
        # expression translation to RPN
        expr_in_opn = opn(temp_expr)

        set_var(var)

        # finding the derivative in expanded form
        diff_in_opn = diff(expr_in_opn)

        # derivative simplification
        simplify_diff = simplify_expr(diff_in_opn)

        # converting an expression into a mathematical form
        res_in_math_form = from_opn(simplify_diff)
        temp_expr = res_in_math_form

    return temp_expr


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Diff',
                                     description='Finding the derivative of a function of one variable of any order'
                                                 ' and finding the partial derivative of a function of two variables.',
                                     epilog='''
        The logarithm is written as log(2)(3x), where (2) is the base 
        (mandatory in brackets), (3x) is the argument. 
        Multiplication signs can miss only between numeric factors 
        and expression/variable/brackets. Wrong: (56xy/(12x-1))(2xsin(y)+4). 
        Correct: (56x*y/(12x-1))*(2x*sin(y)+4). 
        Negative numbers are entered in the form (0-3).''')
    parser.add_argument('input', type=str, help='Expression for differentiation')
    parser.add_argument('-var', type=str, default='x',
                        help='Name of variable for getting partial derivative (default - x)')
    parser.add_argument('-ord', type=int, default=1, help='Derivative order (default - 1)')
    args = parser.parse_args()

    print(process(args.input, args.ord, args.var))
