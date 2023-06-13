import argparse

from Differentiation import diff, simplify_expr, set_var
from Rpn import opn, from_opn, get_list_of_operations_and_operands
from Incorrect_input import input_is_correct


def process(inp, var='x'):
    # input validation
    inp_is_corr = input_is_correct(get_list_of_operations_and_operands(inp))
    if not inp_is_corr[0]:
        return f'Input is wrong! Position error: {inp_is_corr[1]}.'

    # expression translation to RPN
    expr_in_opn = opn(inp)

    set_var(var)

    # finding the derivative in expanded form
    diff_in_opn = diff(expr_in_opn)

    # derivative simplification
    simplify_diff = simplify_expr(diff_in_opn)

    # converting an expression into a mathematical form
    res_in_math_form = from_opn(simplify_diff)

    return res_in_math_form


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Diff',
                                     description='Finding the derivative of a function of one variable'
                                                 ' and finding the partial derivative of a function of two variables.',
                                     epilog='For osnfsjn')
    parser.add_argument('input', type=str, help='Expression for differentiation')
    parser.add_argument('--var', type=str, default='x',
                        help='Name of variable for getting partial derivative (default - x)')
    args = parser.parse_args()

    print(process(args.input, args.var))
    # print('Hi')
