from Differentiation import diff, simplify_expr
from Rpn import opn, from_opn, get_list_of_operations_and_operands
from Incorrect_input import input_is_correct


def process(inp):
    # проверка корректности ввода
    inp_is_corr = input_is_correct(get_list_of_operations_and_operands(inp))
    if not inp_is_corr[0]:
        return f'Input is wrong! Position error: {inp_is_corr[1]}.'

    # перевод выражения в ОПН
    expr_in_opn = opn(inp)

    # нахождение производной в развернутом виде
    diff_in_opn = diff(expr_in_opn)

    # упрощение производной
    simplify_diff = simplify_expr(diff_in_opn)

    # перевод выражение в математический вид
    res_in_math_form = from_opn(simplify_diff)

    return res_in_math_form


if __name__ == '__main__':
    input = '2x^4+17'
    print(process(input))
