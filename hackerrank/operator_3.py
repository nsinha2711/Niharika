#Objective
#In this challenge, you'll work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video!

#Task
#Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

#Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

#Input Format

#There are  lines of numeric input:
#The first line has a double,  (the cost of the meal before tax and tip).
#The second line has an integer,  (the percentage of  being added as tip).
#The third line has an integer,  (the percentage of  being added as tax).

#Output Format

#Print the total meal cost, where  is the rounded integer result of the entire bill ( with added tax and tip).


mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

tip_cost = (tipPercent/100.)* mealCost
tax_cost = (taxPercent/100.)* mealCost
totalCost = int(round(mealCost + tip_cost + tax_cost))
print(totalCost)
