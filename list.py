my_list = ['apples', 6, 'bananas', 12]
print(my_list)
my_list.append('limes')
print(my_list[3])
print(my_list[-1])
print(my_list.index('bananas'))
len(my_list)
my_list.remove('limes')
my_list.pop(0)
my_list.pop()
my_list[0] = 7   # modify a list

my_tuple = ('apples', 'bananas')  # cannot be modified
my_list.insert(0, 'was')
print(my_list)
