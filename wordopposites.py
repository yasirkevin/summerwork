import random

# rushed

words = "hot, summer, hard, dry, simple, light, weak, male, sad, win, small, ignore, buy, succeed, reject, prevent, exclude, top, useless, stand".split(", ")
opposites = "cold, winter, soft, wet, complex, darkness, strong, female, happy, lose, big, pay attention, sell, fail, accept, allow, include, bottom, useful, sit".split(",")

wordsNumber = len(words)
score = 0

for i in range(1, 11):
  random1 = random.randint(0, len(words) - 1)
  
  print("Q{}: {} is to {}".format(i, words[random1], opposites[random1]))
  words.remove(words[random1])
  opposites.remove(opposites[random1])

  random2 = random.randint(0, len(opposites) - 1)
  userInput = input("as {} is to ".format(opposites[random2]))
  
  if userInput.upper() == words[random2].upper():
      score += 1
      
  words.remove(words[random2])
  opposites.remove(opposites[random2])

print(score)
      


