# While statement

product = 3

while product <= 50:
    product *= 3
    print(product)

# for statement
for character in 'Programming':
    print(character, end=' ')

#__________________________________________________________________________________________________________________________________________________________________
total = 0
list = [2, -3, 0, 17, 9]
for number in list:
    total = total + number 
    print(total, '\t', end='')

#___________________________________________________________________________________________________________________________________________________________________
for counter in range(10):
    print(counter, end=' ')


#___________________________________________________________________________________________________________________________________________________________________
total = 0
for number in [1, 2, 3, 4, 5]:
    total += number # add number to total


#___________________________________________________________________________________________________________________________________________________________________
# Sequence-Controlled iteration

# class_average.py
"""Class average program with sequence-controlled iteration."""
"""Consider the following requirements statement:

A class of ten students took a quiz. Their grades (integers in the range 0 – 100) are
98, 76, 71, 87, 83, 90, 57, 79, 82, 94. Determine the class average on the quiz.
The following script for solving this problem keeps a running total of the grades, calculates
the average and displays the result. """

# initialization phase
total = 0 # sum of grades
grade_counter = 0
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94] # list of 10 grades

# processing phase
for grade in grades:
    total += grade # add current grade to the running total
    grade_counter += 1 # indicate that one more grade was processed 

# termination phase
average = total / grade_counter
print(f'Class average is {average}')

#___________________________________________________________________________________________________________________________________________________________________

# initialization phase
total = 0 # sum of grades
grade_counter = 0

# processing phase
grade = int(input('Enter grade, -1 to end: ')) # get one grade

while grade != -1:
    total += grade 
    grade_counter += 1 
    grade = int(input('Enter grade, -1 to end: '))

# termination phase
if grade_counter != 0:
    average = total / grade_counter
    print(f'Class average is {average: .2f}')
else:
    print('No grades were entered')

#___________________________________________________________________________________________________________________________________________________________________
amount = 132.54

print(f'{amount:.5f}')

#___________________________________________________________________________________________________________________________________________________________________
# Compund-Interest Calculation
"""We will compute compound interest using the Decimal type for precise monetary calculation."""

# Problem Statement
"""A person invests $1000 in a savings account yielding 5% interest. Assuming that
the person leaves all interest on deposit in the account, calculate and display the
amount of money in the account at the end of each year for 10 years"""

"""Use the following formula for determining these amounts:
a = p(1 + r)^n
where
p is the original amount invested (i.e., the principal),
r is the annual interest rate,
n is the number of years and
a is the amount on deposit at the end of the nth year
"""

# Calculation
principal = 1000
rate = 0.05
n = year = 0
for year in range(1, 11):
    amount = principal * (1 + rate) ** year
    print(f'{year:>2}{amount:>10.2f}')


#___________________________________________________________________________________________________________________________________________________________________
# Break and Continue Statements
for number in range(110):
    if number == 10:
        break
    print(number, end= ' ')

#___________________________________________________________________________________________________________________________________________________________________
for n in range(10):
    if number == 5:
        continue
    print(n, end= ' ')

#___________________________________________________________________________________________________________________________________________________________________
# Random-number Generation
"""Rolling a Six-Sided Die"""
import random

#from functions_tutorial import my_function

for roll in range(10):
    print(random.randrange(1, 7),'\n')

#___________________________________________________________________________________________________________________________________________________________________
# 6,000,000 Rolls
# fig04_01.py
"""Roll a six-sided die 6,000,000 times."""
import random

# face frequency counters
freq1 = 0
freq2 = 0
freq3 = 0
freq4 = 0
freq5 = 0
freq6 = 0

# 6,000,000 die rolls
for roll in range(6_000_000): # note underscore separators
    face = random.randrange(1, 7)

    # increment appropriate face counter
    if face == 1:
        freq1 += 1
    elif face == 2:
        freq2 += 1
    elif face == 3:
        freq3 += 1
    elif face == 4:
        freq4 += 1
    elif face == 5:
        freq5 += 1
    elif face == 6:
        freq6 += 1

print(f'Face{"Frequency":>13}')
print(f'{1:>4}{freq1:>13}')
print(f'{2:>4}{freq2:>13}')
print(f'{3:>4}{freq3:>13}')
print(f'{4:>4}{freq4:>13}')
print(f'{5:>4}{freq5:>13}')
print(f'{6:>4}{freq6:>13}')

#___________________________________________________________________________________________________________________________________________________________________
# CASE STUDY: A GAME OF CHANCE
# SYNOPSIS
"""
You roll two six-sided dice, each with faces containing one, two, three, four, five
and six spots, respectively. When the dice come to rest, the sum of the spots on the 
two upward faces is calculated. If the sum is 7 or 11 on the first roll, you win. If
the sum is 2, 3 or 12 on the first roll (called "craps"), you lose (i.e., the "house" 
wins). If the sum is 4, 5, 6, 8, 9 or 10 on the first rill, that sum becomes your 
"point". To win, you must continue  rolling the dice until you "make your point" (i.e.,
roll that same point value). You lose by rolling a 7 before making your point.
"""

# Execution
# fig04_02.py
"""Simulating the dice game Craps."""

import random

def roll_dice():
    """Roll two dice and rreturn their face values as a tuple"""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2) # pack die face values into a tuple

def display_dice(dice):
    """Display one roll of the dice."""
    die1, die2 = dice # unpack the tuple into variables die1 and die2
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')

die_values = roll_dice() # first roll
display_dice(die_values)

# determine game status and point, based on first roll
sum_of_dice =sum(die_values)

if sum_of_dice in (7, 11): # win
    game_status = 'WON'
elif sum_of_dice in (2, 3, 12): # lose
    game_status = 'LOST'
else: # for point
    game_status = 'CONTINUE'
    my_point =sum_of_dice
    print('Point is', my_point)

# Continue rolling until player wins or loses
while game_status == 'CONTINUE':
    die_values = roll_dice()
    display_dice(die_values)
    sum_of_dice = sum(die_values)

    if sum_of_dice == my_point: # win by making point
        game_status = 'WON'
    elif sum_of_dice == 7: # lose by rolling 7
        game_status = 'LOST'

# Display "wins" or "loses" message
if game_status == 'WON':
    print('Player wins')
else:
    print('Player loses')

#___________________________________________________________________________________________________________________________________________________________________
# Visualizing Die-Roll Frequencies and Percentage
# Launching IPython for Interactive Matplotlib Development
#ipython --matplotlib
# Importing the libraries


#___________________________________________________________________________________________________________________________________________________________________
# Counting the Number of Occurrences of an Item- using Count

responses = [1, 2, 2, 3, 2, 1, 3, 3, 4, 1, 4, 2, 2, 3, 1, 1, 4, 3, 2, 1, 1, 1]

for i in range(1, 5):
    print(f'{i} appears {responses.count(i)} times in responses.')

#___________________________________________________________________________________________________________________________________________________________________
