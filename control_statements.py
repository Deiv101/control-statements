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
