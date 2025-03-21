#UNWSP Programming PythonCos2005DEsp25
#Program_4_Course Info
#03.21.25
#Abraham. N. Andersen

def find_courses(course_data, subject):
  """
  This function finds courses with a specific subject.

  Args:
    course_data: A dictionary containing course IDs and names.
    subject: The subject.
  """

  found_courses = []

  for course_id, course_name in course_data.items():
    if course_id.startswith(subject):
      found_courses.append((course_id, course_name))

  return found_courses


course_info = {}

while True:
  course_id = input("Enter a course ID (or type 'done' to finish): ")
  if course_id.lower() == "done":
    break
  course_name = input("Enter the course name: ")
  course_info[course_id] = course_name

search_subject = input("Enter the subject: ")

matching_courses = find_courses(course_info, search_subject.upper())
if matching_courses:
  print("Courses with subject", search_subject.upper() + ":")
  for course_id, course_name in matching_courses:
    print(course_id, "-", course_name)
else:
  print("No courses found with subject", search_subject.upper())