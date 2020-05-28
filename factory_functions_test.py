from factory_functions_def import *

### PART 1 - Regular dough / bread ###
# Test 1  -  make_dough()

print("When make_dough is called with 'water' and 'flour' it should return 'dough'")
print(make_dough('water', 'flour') == 'dough')
print("Output:", make_dough('water', 'flour'))


# Test 2  -  make_dough()

print("When make_dough is called with 'water' and 'cement' it should return 'not dough'")
print(make_dough('water', 'cement') == 'not dough')
print("Output:", make_dough('water', 'cement'))

# Test 3  -  bake_bread()

print("When bake_bread is called with 'dough' it should return 'bread'")
print(bake_bread('dough') == 'bread')
print("Output:", bake_bread('dough'))

# Test 4  -  bake_bread()

print("When bake_bread is called with 'not dough' it should return 'not bread'")
print(bake_bread('not dough') == 'not bread')
print("Output:", bake_bread('not dough'))

### PART 2 - Whole wheat dough / bread ###
# Test 5  -  make_ww_dough()

print("When make_ww_dough is called with 'water' and 'whole wheat flour' it should return 'whole wheat dough'")
print(make_ww_dough('water', 'whole wheat flour') == 'whole wheat dough')
print("Output:", make_ww_dough('water', 'whole wheat flour'))

# Test 6  -  bake_ww_bread()

print("When bake_ww_bread is called with 'whole wheat dough' it should return 'whole wheat bread'")
print(bake_ww_bread('whole wheat dough') == 'whole wheat bread')
print("Output:", bake_ww_bread('whole wheat dough'))
