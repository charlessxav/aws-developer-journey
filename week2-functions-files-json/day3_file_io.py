
# Writing to a file in Python
with open("study_plan.txt", "w") as file:
    file.write("Day 1 of Learning\n")
    file.write("Day 2 of Learning\n")
    file.write("Day 3 of Learning\n")
    
# Appending to a file in Python
with open("study_plan.txt", "a") as file:
    file.write("Day 4 of Learning\n")

# Reading from a file in Python
with open("study_plan.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)  
