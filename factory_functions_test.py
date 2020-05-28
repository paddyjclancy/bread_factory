from factory_functions_def import *

# Test 1

print("When make_dough is called with 'water' and 'flour' it should return 'Dough'")
print(make_dough('water', 'flour') == 'Dough')
print("Got:", make_dough('water', 'flour'))


# Test 2

print("When make_dough is called with 'water' and 'cement' it should return 'not dough'")
print(make_dough('water', 'cement') == 'Not dough')
print("Got:", make_dough('water', 'cement'))