#Reads a text file named numbers.txt
with open("D:\[CMPE103] OOP\Integer_Extraction\\numbers.txt") as source:
    #Identifies whether the numbers are odd or even
    for line in source:
        strtoint=int(line)
        #Determines if the numbers present are odd or even
        if strtoint%2==0:
        else:
#Creates a text file for the odd numbers
#Creates a text file for the even numbers