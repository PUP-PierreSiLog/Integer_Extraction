#Reads a text file named numbers.txt, and create a text file for the odd and even integers
with open("D:\[CMPE103] OOP\Integer_Extraction\\numbers.txt") as source, open("D:\[CMPE103] OOP\Integer_Extraction\\Odd.txt", "a") as odd_output, open("D:\[CMPE103] OOP\Integer_Extraction\\even.txt", "a") as even_output:
    #Identifies whether the numbers are odd or even
    for line in source:
        strtoint=int(line)
        #Determines if the numbers present are odd or even
        if strtoint%2==0:
            strtoint=str(strtoint)
            even_output.write(strtoint+"\n")
        else:
            strtoint=str(strtoint)
            odd_output.write(strtoint+"\n")
