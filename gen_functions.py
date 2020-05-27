# Defining a function
#       Return, not print
def say_hello_name(name):
    return(f'Hello, {name}')

# The following is BAD:
#
#     def return_formatted_name(name):
#         print(name.title().strip())
#         return None
#
# Preferred:

def return_formatted_name(name):
    return name.title().strip()

f_name = return_formatted_name("  pAtrICk      ")

print(say_hello_name(f_name))