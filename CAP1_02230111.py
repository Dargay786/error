################################
# Tshering Dargay
# 1ECE
# 02230111
################################
# REFERENCES
# Links that you referred while solving
# the problem
# http://link.to.an.article/video.com
################################
# SOLUTION
# Your Solution Score:
# Put your number here
################################
def read_input(file_path):
    with open(file_path, 'r') as file:
        rounds = [line.strip().split() for line in file] 
    return rounds

def calculate_score(rounds):
    total_score = 0  # Initialize total score
    # Calculate score based on the combination of shape and outcome
    for shape, outcome in rounds:  # Iterate over each shape-outcome pair
        if shape == 'A' and outcome == 'X':
            total_score += 3  # Add 3 to the total score if shape is A and outcome is X
        elif shape == 'A' and outcome == 'Y':
            total_score += 4  # Add 4 to the total score if shape is A and outcome is Y
        elif shape == 'A' and outcome == 'Z':
            total_score += 8  # Add 8 to the total score if shape is A and outcome is Z
        elif shape == 'B' and outcome == 'X':
            total_score += 1  # Add 1 to the total score if shape is B and outcome is X
        elif shape == 'B' and outcome == 'Y':
            total_score += 5  # Add 5 to the total score if shape is B and outcome is Y
        elif shape == 'B' and outcome == 'Z':
            total_score += 9  # Add 9 to the total score if shape is B and outcome is Z
        elif shape == 'C' and outcome == 'X':
            total_score += 2  # Add 2 to the total score if shape is C and outcome is X
        elif shape == 'C' and outcome == 'Y':
            total_score += 6  # Add 6 to the total score if shape is C and outcome is Y
        elif shape == 'C' and outcome == 'Z':
            total_score += 7  # Add 7 to the total score if shape is C and outcome is Z
    return total_score  # Return the total score

file_path = "input_5_cap1.txt"  # Path to the input file

# Read combinations from the file
 # Create a list of shape-outcome pairs
rounds = read_input(file_path)

total_score = calculate_score(rounds)  # Calculate total score using calculate_score function
print("Total Score:", total_score)  # Print the total score
