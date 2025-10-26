my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': ['a', 'b', 'c', 'd', 'e'],
    'dict': {'cat': 'meow', 'dog': 'gav', 'cow': 'moo', 'duck': 'crya', 'sheep': 'bee'},
    'set': {'Tom', 'Mike', 'Bob', 'Sam', 'Phil'} 
    }

print(my_dict['tuple'][-1])

my_dict['list'].append('f')
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = 'tuptup'
my_dict['dict'].pop('duck')

my_dict['set'].add('Henry')
my_dict['set'].remove('Tom')

print(my_dict)
