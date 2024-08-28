def print_params(a=1, b='Строка', c=True):
    print(a, b, c)


print_params(1, 'Строка', True)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])


values_list = [54.32, 'Строка', 42]
values_dict = {'a': 1, 'b': 'Строка', 'c': True}
print_params(**values_dict)
print_params(*values_list)


values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
