# helper.py contains helper functions that can be used by all files in the project

# keep asking for a response until they give an acceptable response
def askPrompt(prompt, answers):
  for i in range(len(answers)):
    answers[i] = answers[i].title()
  print(prompt)
  print("Acceptable answers: " + str(answers))
  response = input().title()
  print("your response: " + response)
  print(answers)
  while response not in answers:
    print("Invalid response: " + response)
    response = input(prompt+"\n").title()
  return response

# coordinates for moving around in the overworld
#def coordinates(roomRow, roomCol):
  # roomRow is horizontal, while roomCol is vertical.
  # Examples:
  # currentRoom = [1, 3]
  # currentRoom[1] += 1
currentRoom = [0, 2]