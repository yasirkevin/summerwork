import random

QUESTIONS = 10

invalidCharacters = ",[]_-\\"
data = [
  # [[KEY], [SYNONYMS], [ANTONYMS]]
]
score = 0

###### WORD DATA PARSER ######
# Can be optimized
with open('data_oppositewords.txt') as f:
    allLines = f.readlines()

    for line in range(1, len(allLines)):
        content = allLines[line]

        if ("KEY:" in content):
          wordEnd = content.find(".")
          word = content[5: wordEnd]
          foundInvalid = False

          for i in range(len(invalidCharacters)):
            if invalidCharacters[i] in word or len(word) <= 2:
                foundInvalid = True

          if foundInvalid:
            continue

          data.append([[word], [], []])      

        elif ("SYN:" in content):
          words = content[5: content.find(".") or len(content)].split(", ")
          
          for word in words:
            foundInvalid = False
            if foundInvalid:
              continue

            for char in invalidCharacters:
              if char in word:
                foundInvalid = True
                words.remove(word)
                break

          data[len(data) - 1][1] = words

        elif ("ANT:" in content):
          words = content[5: content.find(".") or len(content)].split(", ")
          
          for word in words:
            foundInvalid = False
            if foundInvalid:
              continue

            for char in invalidCharacters:
              if char in word:
                foundInvalid = True
                words.remove(word)
                break
        

          data[len(data) - 1][2] = words

    
####


for questionNumber in range(QUESTIONS):
  while True:
    firstRandomWord =  data[random.randint(0, len(data) - 1)]

    if len(firstRandomWord[2]) > 2:
      firstRandomAnt = firstRandomWord[2][random.randint(0, len(firstRandomWord[2]) - 1)]
      break

  while True:
    secondRandomWord = data[random.randint(0, len(data) - 1)]
    #print(secondRandomWord[0][0], firstRandomWord[0][0])
    if secondRandomWord != firstRandomWord:
      break
  
  answer = input("Q{}: {} is to {}, as {} is to "
  .format(questionNumber + 1, firstRandomWord[0][0].upper(), firstRandomAnt.upper(), secondRandomWord[0][0].upper()))

  if answer.upper() in secondRandomWord[2]:
    score += 1

print("Score: {}".format(score))



  


