# Create a dictionary to store user's input
user_info = {}

# Create a loop for the name
while True:
    input_name = input("Please input a name: ")

    # Create a loop for the age, inside the first loop
    while True:
        try:
            input_age = int(input("Please input age: "))
            break  # If age is valid, break out of this loop
        except:
            print("Please input a valid number for age.") # If age is not valid, print an error message

    # Create a loop for the retry confirmation

    # Ask if the user wants to input another entry using a variable, if not, break the loop
# Create oldest_name and oldest_age variables, store the first input of the user (index 0)
# Compare the age in oldest_age to the current age (new entry)
    # If the new information/input is greater than the age in oldest_age variable, update oldest_age and oldest_name
    #Print the oldest person using a function that will print the oldest_name and oldest_age