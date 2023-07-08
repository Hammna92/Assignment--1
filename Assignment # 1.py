#Assignment no. 1-A

Student_name = input("Enter Student Name: ")
Roll_number =  int (input ("Enter Roll number: "))
Standard = int (input ("Enter Standard: "))   
English = int (input ("Enter English Marks: ")) 
Math = int (input ("Enter Math Marks: ")) 
Islamiat = int (input ("Enter Islamiat: ")) 
Marks_Obtained = English + Math + Islamiat
print (Marks_Obtained)
Total_Marks = 300
perc = (Marks_Obtained / Total_Marks)*100
print (perc)
if perc <=100 and perc >= 80:
    print("Grade: A+")
elif perc <=80 and perc >=70:
    print("Grade: A")
elif perc <=70 and perc >=60:
    print("Grade: B")
elif perc <= 60 and perc >=50:
    print("Grade: C")
elif perc <=50 and perc >=40:
    print("Grade: D")
elif perc <100 or perc > 0:
    print ("Put the correct grade")
else:
    print ("Result: Fail")