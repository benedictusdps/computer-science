last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Create list of classes called subject
subjects = ["physics", "calculus", "poetry", "history"]
# Create list of grades for each classes
grades = [98, 97, 85, 88]
# Create list with both subject and grades
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Add a new subject
gradebook.append(["computer science", 100])
# Add another new subject
gradebook.append(["visual arts", 93])
# Change the score for visual arts to 98
gradebook[-1][-1] = 98

# Remove grades for poetry and change to Pass
gradebook[2].remove(85)
gradebook[2].append("Pass")

# Combine current gradebook with last semester's gradebook
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)