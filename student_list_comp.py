#! python
# List Comprehension
# Program to contains student names, favorite subject, test score
# Compress the three

students = ['Andile', 'Jaden', 'Mzie-Michael', 'Proud', 'Eric', 'Nandipa', 'Phumz', 'Nokuzola']
fav_subject = ['Computing', 'Design', 'Literature', 'Chemistry', 'Mathematics', 'Biology', 'Mathematics', 'Physics']
scores = [90, 88, 95, 91, 99, 90, 89, 92]

combined = zip(students, fav_subject, scores)
students_info = list(combined)

for student in students_info:
    print("{}'s favorite subject is {} and they last scored {}".format(*student))
