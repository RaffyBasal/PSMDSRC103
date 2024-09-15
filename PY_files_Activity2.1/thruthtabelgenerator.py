def generate_truthtable(number_of_variables=None):
    # Prompt for input if no value is provided
    if number_of_variables is None:
        number_of_variables = int(input("Please enter the number of variables: "))
    
    if number_of_variables <= 0:
        return "You need to enter an integer."
    else:
        total_combinations = 2 ** number_of_variables
        combination_list = []

        for i in range(total_combinations):
            bin_equivalent = bin(i)[2:].zfill(number_of_variables)  # Using zfill to pad with zeros
            combination_list.append(tuple(int(val) for val in bin_equivalent))
        return combination_list

#main program
def evaluate_propositional_logic(combination_list):
    # Input the propositional logic expression from the user
    expression = input("Enter the propositional logic expression (use variables A, B, and C): ")

    # Iterate over each combination of truth values
    for row in combination_list:
        # Unpack values to variables A, B, and C (for 2 variables, C will be ignored)
        A, B, C = (row + (0, 0, 0))[:3]  # Add extra zeros to handle 2-variable input
        
        try:
            # Evaluate the expression
            result = eval(expression)
        except Exception as e:
            return f"Error in evaluating expression: {e}"
        
        # Print the truth table row and the result
        print(f"{row} -> {result}")


# Step 2: Evaluate the propositional logic for the generated truth table
evaluate_propositional_logic(generate_truthtable())
