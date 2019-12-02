# Ruben Navarro
# 12/02/2019
# main.py
# CTCI - Check Permutation
# Checks if string is a permutation of another string

def checkPermutation(str, str2):

# checks length of both strings
    if len(str) != len(str2):
        print(" {0} is not a permutation of {1}".format(str2, str))

# sorts both strings
    s = sorted(str)
    s2 = sorted(str2)

# compares each character in both strings using the zip function
    for letter, letter2 in zip(s, s2):
      if letter != letter2:
        print(" {0} is not a permutation of {1}".format(str2, str))
        return False

    print("%s is a permutation of %s." % (str2, str))

str = "testing"
str2 = "ginttes"

checkPermutation(str, str2)
