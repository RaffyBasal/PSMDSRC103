print("Proportional Logic Evaluator for Discrete Math")
variables = int(input("How many variables (2 or 3)? "))
total_combination = 2 ** variables

combination_list = []

# Generate the combinations
for i in range(total_combination):
    bin_equivalent = bin(i)[2:]
    while len(bin_equivalent) < variables:
        bin_equivalent = "0" + bin_equivalent
    combination_list.append(tuple(int(val) for val in bin_equivalent))

# Main Program
expression = input("Enter the propositional logic expression (use A, B, C): ")

"""Note:
        Only the Letters A, B, and C are allowed to be used.
        A sample input would be: not (A and B) or (A and C).
        All input must be CAPITAL cases."""

# Validate variables and expression
if variables == 2:
    print("A B f")
    for A, B in combination_list:
        evaluated_expression = eval(expression.replace('A', str(A)).replace('B', str(B)))
        print(A, B, evaluated_expression)

elif variables == 3:
    print("A B C f")
    for A, B, C in combination_list:
        evaluated_expression = eval(expression.replace('A', str(A)).replace('B', str(B)).replace('C', str(C)))
        print(A, B, C, evaluated_expression)
else:
    print("Only 2 or 3 variables are supported.")



        