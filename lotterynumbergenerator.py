
import random

RANGE = 49
GENERATIONS = 6

numbers = []
inputs = []
numbersIncorrect = GENERATIONS

def check_repeated(num):
  for i in range(1, len(numbers)):
    if numbers[i] == num:
      return True
  return False

for i in range(1, GENERATIONS + 1):
  generatedNumber = random.randint(1, 49)
  userInput = 0
  metConditions = False
  while not(metConditions):
    userInput = ""

    if check_repeated(generatedNumber) == False:
      try:
          userInput = int(input("[{}] Guess the number: ".format(i)))
          metConditions = True
      except ValueError:
          print("[!] Invalid number")
    else:
      generatedNumber = random.randint(1, 49)
  

  numbers.append(generatedNumber)
  inputs.append(userInput)

print("\n The numbers were: \n")

for i in range(0, GENERATIONS):
  if numbers[i] == inputs[i]:
    numbersIncorrect -= 1
    print("[{}] Correct!".format(i + 1))
  else:
    print("[{}] Incorrect! The number was: {}".format(i + 1, numbers[i]))
