def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params(32)
print_params(32, 'Gleb')
print_params(32, 'Gleb', False)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])


values_list = (23, 'one', False)
values_dict = {'a': 1, 'b' : 'строка', 'c': True}


print_params(*values_list)
print_params(**values_dict)


values_list_2 = [33.42, 'студент']
print_params(*values_list_2, 54)
