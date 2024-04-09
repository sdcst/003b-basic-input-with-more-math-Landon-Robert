#

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population

#Enter the population: 25000000
#Enter the rate of growth in percent: 2.1
#Enter the number of days: 12
#There will be 25017087 people after 12 days

POP = int(input("What is the current population?: "))
GR = int(input("What is the population growth rate? (decimal): "))
T = int(input("Enter number of days: "))
FP = POP * (1+GR)**T
print(f"The future population will be {FP}")
