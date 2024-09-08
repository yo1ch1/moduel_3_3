def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list = [12, 'straight', False]
values_dict = {'a': 99, 'b': 'clover', 'c': '13' }
values_list_2 = [54.32, 'Строка' ]

print_params()
print_params(13, 'hello')
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)