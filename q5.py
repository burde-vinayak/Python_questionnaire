import operator as op
def  apply_operator(left_operand, right_operand, operator):
    OPERATORS = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.div}
    return OPERATORS[operator](left_operand, right_operand)

print apply_operator(2,5,'+')