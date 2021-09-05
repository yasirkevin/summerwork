import time
import random

RANGE = 49
GENERATIONS = 6

numbers = []
inputs = []
score = 0

def check_repeated(num):
  for i in range(1, len(numbers)):
    if numbers[i] == num:
      return True
  return False

def probability(score):
  totalProbability = 1

  for i in range(score):
    totalProbability = totalProbability * 1/RANGE
  
  for i in range(GENERATIONS - score):
    totalProbability = totalProbability * (RANGE - 1)/RANGE
  
  return totalProbability

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

print("\nResults: \n")

for i in range(0, GENERATIONS):
  time.sleep(0.05)

  if numbers[i] == inputs[i]:
    score += 1
    print("[{}] Correct!".format(i + 1))
  else:
    print("[{}] Incorrect! The number was: {}".format(i + 1, numbers[i]))

print("\n Combinaton Probability: {}% \n".format(round(probability(score) * 100, 2)))
