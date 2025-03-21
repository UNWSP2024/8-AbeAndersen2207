#UNWSP Programming PythonCos2005DEsp25
#Program_2_Word Separator
#03.21.25
#Abraham. N. Andersen

def fix_sentence(mixed_up_sentence):
  """
  This function takes a sentence where all the words are stuck together,
  like "StopAndSmellTheRoses", and turns it into a normal sentence
  like "Stop and smell the roses".

  Args:
    mixed_up_sentence: The sentence with no spaces.

  Returns:
    The sentence with spaces and lowercase letters (except the first word).
  """

  fixed_sentence = ""
  for i, letter in enumerate(mixed_up_sentence):
    if i == 0:
      fixed_sentence += letter
    elif letter.isupper():
      fixed_sentence += " " + letter.lower()
    else:
      fixed_sentence += letter

  return fixed_sentence

user_input = input("Type in a sentence where all the words are stuck together (like StopAndSmellTheRoses): ")


fixed_result = fix_sentence(user_input)


print("Here's your sentence fixed:", fixed_result)