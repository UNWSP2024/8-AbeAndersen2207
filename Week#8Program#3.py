#UNWSP Programming PythonCos2005DEsp25
#Program_3_Capital Quiz
#03.21.25
#Abraham. N. Andersen

import random

def state_capital_quiz():
  """
  This program quizzes the user on U.S. state capitals.
  """


  state_capitals = {
      "Alabama": "Montgomery",
      "Alaska": "Juneau",
      "Arizona": "Phoenix",
      "Arkansas": "Little Rock",
      "California": "Sacramento",
      "Colorado": "Denver",
      "Connecticut": "Hartford",
      "Delaware": "Dover",
      "Florida": "Tallahassee",
      "Georgia": "Atlanta",
      "Hawaii": "Honolulu",
      "Idaho": "Boise",
      "Illinois": "Springfield",
      "Indiana": "Indianapolis",
      "Iowa": "Des Moines",
      "Kansas": "Topeka",
      "Kentucky": "Frankfort",
      "Louisiana": "Baton Rouge",
      "Maine": "Augusta",
      "Maryland": "Annapolis",
      "Massachusetts": "Boston",
      "Michigan": "Lansing",
      "Minnesota": "Saint Paul",
      "Mississippi": "Jackson",
      "Missouri": "Jefferson City",
      "Montana": "Helena",
      "Nebraska": "Lincoln",
      "Nevada": "Carson City",
      "New Hampshire": "Concord",
      "New Jersey": "Trenton",
      "New Mexico": "Santa Fe",
      "New York": "Albany",
      "North Carolina": "Raleigh",
      "North Dakota": "Bismarck",
      "Ohio": "Columbus",
      "Oklahoma": "Oklahoma City",
      "Oregon": "Salem",
      "Pennsylvania": "Harrisburg",
      "Rhode Island": "Providence",
      "South Carolina": "Columbia",
      "South Dakota": "Pierre",
      "Tennessee": "Nashville",
      "Texas": "Austin",
      "Utah": "Salt Lake City",
      "Vermont": "Montpelier",
      "Virginia": "Richmond",
      "Washington": "Olympia",
      "West Virginia": "Charleston",
      "Wisconsin": "Madison",
      "Wyoming": "Cheyenne"
  }

  correct_count = 0
  incorrect_count = 0


  for _ in range(20):
    state = random.choice(list(state_capitals.keys()))

    user_answer = input(f"What is the capital of {state}? ")

    if user_answer.lower() == state_capitals[state].lower():
      print("Correct!")
      correct_count += 1
    else:
      print(f"Incorrect. The capital of {state} is {state_capitals[state]}.")
      incorrect_count += 1


  print(f"\nYou got {correct_count} correct and {incorrect_count} incorrect.")


state_capital_quiz()