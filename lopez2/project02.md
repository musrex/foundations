# Assignment 2 Write Up
This program takes in two inputs from a user, and runs them through a function that determines whether the inputs are evenly divisible by each other. If the numbers are evenly divisible, TRUE is returned. If not, the user is prompted to try again.

# Assignment 2 Algorithm
1. Initiate a loop
2. Input two numbers, a & b
3. Divide a by b, if even return True
4. If step 3 returns True, end loop
5. Divide b by a, if even return True
6. If step 5 returns True, end loop
7. If step 2 or 3 don't return True, return False
8. If False, restart loop