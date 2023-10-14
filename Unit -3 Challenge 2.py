class student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name 
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  # Sort the llist or students in descending order of CGPA
  sorted_students = sorted(student_list,
                         key=lambda student: student.cgpa, 
                         reverse=True) 
  # Syntax - lambda arg:exp
  return sorted_students

# Example usage:
students = [
    student("Hari", "A123", 7.8),
    student("Mohan", "A124", 8.9),
    student("Venkatesh", "A125", 9.1),
    student("Gokul", "A126", 9.9),
]

sorted_students = sort_students(students)

# Print the sorted list or students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number, student.cgpa))