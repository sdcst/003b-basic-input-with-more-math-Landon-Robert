#!python3
 
"""
Assignment 5:
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON_'s Orchard. I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples straight off the tree that tasted like _FOOD_. Then there was a _ADJECTIVE_ apple that looked like a _NOUN_. When our bag was full, we went on a free hay ride to _PLACE_ and back. It ended at a hay pile where we got to _VERB_ _ADVERB_. I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD_ and _THINGS_ pies!
"""
print("Input words to fill in the blanks to complete the Mad Lib ")
V1 = (input("Today we picked apple from _PERSON_'s Orchard. "))
V2 = (input("I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples straight off the tree "))
V3 = (input("that tasted like _FOOD_. "))
V4 = (input("Then there was a _ADJECTIVE_ apple "))
V5 = (input("that looked like a _NOUN_. "))
V6 = (input("When our bag was full, we went on a free hay ride to _PLACE_ and back. "))
V7 = (input("It ended at a hay pile where we got to _VERB_ "))
V8 = (input("_ADVERB_ "))
V9 = (input("I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD_ "))
V10 = (input("and _THINGS_ pies! "))

print(f"Today we picked apple from _{V1}_'s Orchard. I had no idea there were so many different varieties of apples. I ate _{V2}_ apples straight off the tree that tasted like _{V3}_. Then there was a _{V4}_ apple that looked like a _{V5}_.  When our bag was full, we went on a free hay ride to _{V6}_ and back. It ended at a hay pile where we got to _{V7}_ _{V8}_. I can hardly wait to get home and cook with the apples. We are going to make apple _{V9}_ and _{V10}_ pies!")