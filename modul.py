from fractions import Fraction

def add_r(my_str):
    list = my_str.split()
    a = Fraction(list[0])
    b = Fraction(list[1])
    return f'{a} + {b} = {a + b}'

def sub_r(my_str):
    list = my_str.split()
    a = Fraction(list[0])
    b = Fraction(list[1])
    return f'{a} - {b} = {a - b}'

def mult_r(my_str):
    list = my_str.split()
    a = Fraction(list[0])
    b = Fraction(list[1])
    return f'{a} * {b} = {a * b}'

def div_r(my_str):
    list = my_str.split()
    a = Fraction(list[0])
    b = Fraction(list[1])
    return f'{a} / {b} = {a / b}'

def add_c(my_str):
    list = my_str.split()
    a = complex(list[0])
    b = complex(list[1])
    return f'{a} + {b} = {a + b}'

def sub_c(my_str):
    list = my_str.split()
    a = complex(list[0])
    b = complex(list[1])
    return f'{a} - {b} = {a - b}'

def mult_c(my_str):
    list = my_str.split()
    a = complex(list[0])
    b = complex(list[1])
    return f'{a} * {b} = {a * b}'

def div_c(my_str):
    list = my_str.split()
    a = complex(list[0])
    b = complex(list[1])
    return f'{a} / {b} = {a / b}'
