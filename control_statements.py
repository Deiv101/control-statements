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