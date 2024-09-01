def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = (23, 'one', False)
values_dict = {'a': 1, 'b' : 'строка', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [33.42, 'студент']
print_params(*values_list_2, 54)