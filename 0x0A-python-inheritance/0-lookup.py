n1 = 5
n2 = 7

q = "what is " + str(n1)  + "+" + str(n2) + "?" + " ans: " 
user_answer = input(q)
print("your answer is", user_answer)
# Initialize a variable 'full_name' with an empty string
full_name = ""

# Prompt the user to enter their first name and store it in the 'first_name' variable
first_name = input("Enter your first name: ")

# Prompt the user to enter their last name and store it in the 'last_name' variable
last_name = input("Enter your last name: ")

# Concatenate the names with a space in between and store the result in 'my_name'
full_name = first_name + " " + last_name # The `+` symbol can be used to combine two strings.

# Display a message with the user's full name using the 'full_name' variable
print("My name is", full_name)
