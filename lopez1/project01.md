# Assignment 1 Write Up
This program takes in an input from the user, uses that input as the radius,  
and then calculates the circumference, area, and volume of a circle or sphere  
with that radius. For this program, I imported PI from the math module so as 
to have the most accurate PI that I could, and then used that for my calculations.  
I also used a while loop to keep the program running, and TRY and EXCEPT blocks  
for error handling. This way if a user enters something other than a number  
they'll be prompted to try again.   

# Assignment 1 Algorithm  
1. Import appropriate modules (pi from math) to get accurate value for PI
2. Ask the user to input the value for RADIUS 
3. Initiate RUN value as a boolean set to TRUE to run program
4. While program is running (RUN = TRUE), perform calculations.
5. If succesful, return calculations with appropriate text and set RUN to FALSE to end program.
6. If unsuccessful, show an error message and prompt for user input again.
