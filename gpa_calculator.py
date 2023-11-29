print("""
#####################################
# Grade Calculator                    #
#####################################
""")

# Get the number of each subject
bnagla_number = int(input("Enter the mark for Bangla subject: "))
english_number = int(input("Enter the mark for English subject: "))
math_number = int(input("Enter the mark for Math subject: "))
science_number = int(input("Enter the mark for Science subject: "))

# Average the total number
total_number = bnagla_number + english_number + math_number + science_number
average_number = total_number / 4

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


