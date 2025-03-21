#UNWSP Programming PythonCos2005DEsp25
#Program_1_Initials
#03.21.25
#Abraham. N. Andersen

def get_initials(full_name):
  """
  This function takes a full name as input and returns the initials.

  Args:
    full_name: A string containing the person's first, middle, and last names.

  Returns:
    A string containing the person's initials, separated by periods.
  """

  names = full_name.split()

  initials = ""

  for name in names:
    initials += name[0].upper() + ". "

  initials = initials.rstrip(". ")

  return initials

full_name = input("Enter your full name (first middle last): ")

initials = get_initials(full_name)

print("Your initials are:", initials)