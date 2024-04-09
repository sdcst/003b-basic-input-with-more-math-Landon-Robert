#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""

P1 = int(input("\n\nEnter the first price: "))
P2 = int(input("\n\nEnter the second price: "))
P3 = int(input("\n\nEnter the third price: "))
P4 = int(input("\n\nEnter the fourth price: "))
P5 = int(input("\n\nEnter the fifth price: "))
Pt = P1+P2+P3+P4+P5
print(f"Your total is ${Pt}")