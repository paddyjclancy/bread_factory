# This file tests the following function:
def return_formatted_name(name):
    return name.title().strip()

# Set up
input = " paTRicK    "
expected_output = "Patrick"

# Explain
print("Testing function: return_formatted_name() with input = ' paTRicK    ' --> 'Patrick...")

# Actual test: returns either True or False
print(return_formatted_name(input) == expected_output)