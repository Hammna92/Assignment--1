
#Assignment No. 1-B
#Question 1
# Write a python program to print the following string in a spexcific format.

print ("Twinkle, Twinkle, Little star\n\tHow I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\n Twinkle, Twinkle, Little star\n\tHow I wonder what you are ")

"""""
python version(Question 2)
"""""
import sys
print("System Version")
print (sys.version)


#Write a python program to display the current date and time.

import datetime
tod = datetime.datetime.now()
print(tod)


# Area of a circle (Question 4)

radius = float(input("Enter the Radius of Circle:"))
A = 3.147* radius * radius
print ("Area of Circel is:" ,A)


#Write a python program which tskes two inputs from user and print them addition
num1 = int(input("Enter the First number:"))
num2 = int(input("Enter the Second number:"))
sum = (num1 + num2)
print ("the Sum of two number is:" ,sum)

# write a program which take input from user and identify that the given numberis even or odd.
num_1 = int (input ("Enter the number: "))
print (num_1 % 2)
if (num_1 % 2 ==0):
    print (num_1, "is even number")
else: 
    print (num_1, "is odd number")

#write a python program which accept the user's forst and last name and print them in reverse order with a space between them.
F_name = input ("Enter First Name: ")
L_name = input ("Enter last name: ")
print (L_name +" "+ F_name)

#Write a program ehich takes five input from user for different subject's makrs, total it and genrate marksheet using grades.

Student_name = input("Enter Student Name: ")
Roll_number =  int (input ("Enter Roll number: "))
Standard = int (input ("Enter Standard: "))   
English = int (input ("Enter English Marks: ")) 
Math = int (input ("Enter Math Marks: ")) 
Islamiat = int (input ("Enter Islamiat Mark: ")) 
Physic = int(input("Enter Physic Marks: "))
Chemistry = int(input("Enter Chemistry Marks: "))
Marks_Obtained = English + Math + Islamiat + Physic + Chemistry
print (Marks_Obtained)
Total_Marks = 500
perc = (Marks_Obtained / Total_Marks)*100
print (perc)
if perc <=100 and perc >= 90:
    print("Grade: A+")
elif perc <=90 and perc >=80:
    print("Grade: A")
elif perc <=80 and perc >=70:
    print("Grade: B+")
elif perc <=70 and perc >=60:
    print("Grade: B")
elif perc <= 60 and perc >=50:
    print("Grade: C+")
elif perc <=50 and perc >=40:
    print("Grade:D (Fail)")
elif perc <100 or perc > 50:
    print ("Put the correct grade")
else:
    print ("Result: Fail")


