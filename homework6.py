my_dict = {'Masha' : 2002, 'Petya' : 2001, 'Vasya' : 1996, 'Alina' : 1997}
print(my_dict)
print(my_dict .get('Vasya'))
print(my_dict .get('Lena'))
my_dict['Denis'] = 2000
my_dict['Lena'] = 1998
print(my_dict)
new = my_dict.pop('Masha')
print(new)
print(my_dict)

my_set = {'Line' , 1, 2, 3, 5, 5, (3, 2, 8), True}
print(my_set)
print(my_set.add(9))
print(my_set.add('Apple'))
print(my_set)
print(my_set.discard(5))
print(my_set)



