# # Lab: Anagram detector
#
# ###### Delivery Method: Doctests
# ------------------------------
#
# #### Goal
#
# Write a python program that can detect two words that are anagrams.
#
# -------------------------------
#
# #### Instructions
#
# An anagram is the result of rearranging the letters of a word or phrase to produce a new word or phrase, using
# all the original letters exactly once; for example, the word anagram can be rearranged into "nag a ram".



str1 = str(input("Enter a word or phrase: "))
str2 = str(input("Enter another word or phrase: "))


def is_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        print("This is an anagram")
    else:
        print("This is not an anagram")

is_anagram(str1, str2)
    # x1 = sorted(str1)
    # y1 = sorted(str2)
    #
    # if (x1) == (y1):
    #     print("Anagram is True")
    # else:
    #     print("Anagram is False")



# >>> anagram('abc','bca')
# Anagram is True
#     print("This is an anagram")
# else:
#     print("This is not an anagram")