>>> from hw2 import *

######## Problem 1 ##########
1) Write a function printMultiples(lst) takes a list of numbers and PRINTS the number if it is a multiple of 8

>>> printMultiples([2, 3, 4, 5, 6, 7, 8, 9])
8
>>> printMultiples([8, 16, 32])
8
16
32
>>> printMultiples([100, 56, 24, 3, 32, 7, 16])
56
24
32
16

######## Problem 2 ##########
2) Write a function printSquares(n) that takes an integer n and PRINTS the squares of all numbers from 0 up to, but not including, n.

>>> printSquares(2)
0
1
>>> printSquares(4)
0
1
4
9
>>> printSquares(3)
0
1
4

######## Problem 3 ##########
3) Write a function pay(wage, hours) that takes as input two arguments, an hourly wage and the number of hours an employee worked in the last week. 
Your function should RETURN the employee’s pay. Any hours worked beyond 40 is overtime and should be paid at 1.5 times the regular hourly wage.

>>> pay(15.00, 40)
600.0
>>> pay(10.0, 60)
700.0
>>> pay(17.50, 10)==175.0
True
>>> pay(20.00, 120)
3200.0

######## Problem 4 ##########
4) Write a function abbreviation(day) that takes a day of the week as input and RETURNS its two-letter abbreviation.

>>> abbreviation('Tuesday')
'Tu'
>>> abbreviation('Saturday')=='Sa'
True
>>> abbreviation('Monday')
'Mo'


######## Problem 5 ##########
5) Write a function reverseInt(n) that takes a three-digit integer as input and RETURNS the integer obtained by reversing its digits. 
You can assume ((n>=100) and (n<=999)). For an extra challenge, see if you can do it without converting n to a string.

>>> reverseInt(123)
321
>>> reverseInt(908)
809
>>> reverseInt(888)==888
True


######## Problem 6 ##########
6) Write a function lastF(firstName, lastName) that takes as input two strings and RETURNS a string of the form 'lastName, F.'
Only the first initial should be displayed

>>> lastF('Albert', 'Camus')
'Camus, A.'
>>> lastF('Grace', 'Hopper')
'Hopper, G.'
>>> lastF('Marie', 'Curie')
'Curie, M.'


######## Problem 7 ##########
7) Write a function isNearby(x0, y0, x1, y1) that takes as input 4 numbers defining the location of two points on a Cartesian plot, such that
one point resides at (x0, y0) and the other resides at (x1, y1). 
The function should RETURN True if the distance between the two points is <=10. Otherwise, RETURN False. 
Hint: to calculate the distance between two points -- https://www.wikihow.com/Find-the-Distance-Between-Two-Points

>>> isNearby(0, 0, 0, 10)
True
>>> isNearby(4, -4, -4, 4)
False
>>> isNearby(4, 4, -4, 4)
True
>>> isNearby(4, 4, -4, -4)
False
>>> isNearby(-1, -1, -1, 1)==True
True
>>> isNearby(-10, 0, 10, 0)
False

