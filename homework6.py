my_dict = {'Ольга' : 1993, 'Владимир' : 1989, 'Майя' : 2019}
print('Dict: ',my_dict)
print('Existing value: ', my_dict.get('Владимир'))
print('Not existing value: ', my_dict.get('Кира'))
my_dict.update({'Татьяна' : 1969, 'Олег' : 1968})
a = my_dict.pop('Владимир')
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict)
print(' ')
my_set = {4, 8, 105, 'ворона', 8, 'собака', 105, True, 105, 4, 'ворона', True}
print('Set:' , my_set)
my_set.update({165, False})
my_set.remove(4)
print('Modified set:', my_set)

