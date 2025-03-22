# Coding starts here.

# Ask the user for their grade percentage
grade_percentage = int(input("Enter your grade percentage: "))

# Determine the letter grade
if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"

# Check if the user passed or failed
if grade_percentage >= 70:
    print(f"Congratulations! You passed the course with a grade of {letter}.")
else:
    print(f"Sorry, you did not pass the course. Your grade is {letter}. Best of luck next time!")

# Adding of + sign or - sign to the letter grade
# Determine the grade sign (+ or -)
if letter != "F":  # F does not have a + or -
    last_digit = grade_percentage % 10  # Get the last digit
    if last_digit >= 7:
        sign = "+"
    elif last_digit < 3:
        sign = "-"
    else:
        sign = ""
    
    # Final grade with sign
    final_grade = letter + sign
    print(f"Your final grade is {final_grade}.")
else:
    print(f"Your final grade is {letter}.")  
print("-------------------------------------------------------")
