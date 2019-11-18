


def palindrome(word):
  if len(word) <= 1:
    print("True")
    return True
  if word[0] == word[len(word) - 1]:
    return palindrome(word[1: - 1])
  else:
    print("False")
    return False

palindrome('racecar') #== True)
palindrome('Noon') #== True)
palindrome('ciVic') #== True)
palindrome('nice') #== False)
palindrome('434') #== True)
palindrome('123') #== False)
palindrome('bomb') #== False)


