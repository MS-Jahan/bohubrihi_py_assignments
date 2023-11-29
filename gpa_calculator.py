print("""
#####################################
# Grade Calculator                    #
#####################################
""")

# Get the number of each subject
bangla_number = int(input("Enter the mark for Bangla subject: "))
english_number = int(input("Enter the mark for English subject: "))
math_number = int(input("Enter the mark for Math subject: "))
science_number = int(input("Enter the mark for Science subject: "))

# Validate the number
if bangla_number > 100 or bangla_number < 0:
    print("Invalid number for Bangla subject")
    exit()
elif english_number > 100 or english_number < 0:
    print("Invalid number for English subject")
    exit()
elif math_number > 100 or math_number < 0:
    print("Invalid number for Math subject")
    exit()
elif science_number > 100 or science_number < 0:
    print("Invalid number for Science subject")
    exit()

# Average the total number
average_number = (bangla_number + english_number + math_number + science_number) / 4

# Print the result
if average_number >= 91 and average_number <= 100:
    print("Your grade is A+")
elif average_number >= 81 and average_number <= 90:
    print("Your grade is A")
elif average_number >= 71 and average_number <= 80:
    print("Your grade is B")
elif average_number >= 61 and average_number <= 70:
    print("Your grade is C")
elif average_number >= 41 and average_number <= 60:
    print("Your grade is D")
elif average_number >= 0 and average_number <= 40:
    print("Your grade is F")


