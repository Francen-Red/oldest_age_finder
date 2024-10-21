# Create a dictionary to store user's input
user_info = {}

# Create a list of invalid characters for the name
invalid_characters = [63, 123, 125, 91, 93, 36, 42, 37, 33, 38, 64, 94, 124, 92, 47, 60, 62] # Use ASCII values to avoid confusion or error

# Create a loop for the name
while True:
    input_name = input("Please input a name: ")

    if any(ord(char) in invalid_characters for char in input_name):  # Check if the ASCII values of the name include invalid characters using ord() function
        print("Please input a valid name.")  # If yes, ask the user again for a valid name
        continue 

    # Create a loop for the age, inside the first loop
    while True:
        try:
            input_age = int(input("Please input age: "))
            break  # If age is valid, break out of this loop
        except:
            print("Please input a valid number for age.") # If age is not valid, print an error message

    # Create a loop for the retry confirmation   
    while True:
        confirm = input(f"Name = {input_name}, Age = {input_age}. Is this correct? (yes or no): ") # Use a function to display the user's input
        if confirm == "yes":
            break  # Move on if user confirms that the input is correct
        elif confirm != "yes": 
            retry_choice = input("Retry name, age, or both? (name/age/both): ") # If not, ask the user if they want to retry name, age, or both
            
        while True:
            if retry_choice == "name":
                input_name = input("Please input a new name: ")
                if any(ord(char) in invalid_characters for char in input_name):  # Check if the ASCII values of the name include invalid characters using ord() function
                    print("Please input a valid name.")  # If yes, ask the user again for a valid name
                continue 

            elif retry_choice == "age":
                while True:
                    try:
                        input_age = int(input("Please input a new age: "))
                        break
                    except:
                        print("Please input a valid number for age.")

                break

            
    break  # Move on if the name is valid
    
    # Ask if the user wants to input another entry using a variable, if not, break the loop
# Create oldest_name and oldest_age variables, store the first input of the user (index 0)
# Compare the age in oldest_age to the current age (new entry)
    # If the new information/input is greater than the age in oldest_age variable, update oldest_age and oldest_name
    # Print the oldest person using a function that will print the oldest_name and oldest_age

