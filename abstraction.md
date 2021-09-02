_**A palindrome is a word that reads identically backward or forward. Consider the word
“RACECAR”, what steps would you take to identify whether it was a palindrome? Write
these down using concrete terms. Do the same for another word “DEFIED”.**_

### METHODS ###


1. For each letter in the first half of the word, identify the the opposite letter in the other half (For example: in "DEFIED", first letter is R and the last letter is D, the second letter is E and the second last letter is E, and so forth)
2. if the letter and the opposite letter are the same, continue with the next letter. Otherwise, the word is not a palindrome. (For example: in "DEFIED" the thrd letter and the third last letter are "F" and "I" so it is not a palindrome)

```pseudocode
word = "DEFIED"
word_length = length(word)

FOR letterNumber --> (1 TO ROUND(word_length / 2)) DO
  IF NOT (word[letterNumber] == word[word_length - letterNumber]) THEN
    OUTPUT("Not palindrome")
    QUIT
  ENDIF
ENDFOR

OUTPUT("Palindrome")
  
```

