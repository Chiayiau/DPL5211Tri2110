# Student ID : 1201200302 #
# Student Name : Liang Chia Yiau #
import math

print("Invoice for Fruits Purchase")
print("---------------------------------")

comb = float(input("Enter the quanlity (comb) of bananas bought :"))
kg = float(input("Enter the amount (kg) of grapes bought :"))
banana=1.5
grapes=5.6

print("Item           Qty   Price    Total")
print("Banana (combs)",comb,"  RM{:.2f}   RM{:.2f}".format(banana,comb*banana))
print("Grapes (kg)   ",kg,"  RM{:.2f}   RM{:.2f}".format(grapes,kg*grapes))
print("Total : RM{:.2f}".format(comb*banana + kg*grapes))