# Activity 1
student_list = ['pam','rob','joe','greg','bob','amy','matt']
# The following print statement includes elements at index 2 & excludes element at index 5
print(student_list[2:5])

# print elements beginning to 4th
print(student_list[:-5])

# print elements 6th to end (index 5)
print(student_list[5:])

# print elements beginning to end
print(student_list)
# check if rob is in the student_list
if student_list.count('rob'):
    print("rob exists")
else:
    print("rob does not exist")

