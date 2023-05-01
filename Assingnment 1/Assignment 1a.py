name = input ("Enter name: ")
family = input ("Enter last name: ")
Math = int (input ("Enter your math score: "))
Physics = int (input ("Enter your physics score: "))
History = int (input ("Enter your history score: "))
average = (Math + Physics + History) / 3
if average >= 17:
    print ("Educational Status: Great")
if 12 <= average < 17:
    print ("Educational Status: Normal")
if average < 12:
    print ("educational status: Fail")