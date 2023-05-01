name = input ("Enter name: ")
family = input ("Enter last name: ")
Math = int (input ("Enter your math score: "))
Physics = int (input ("Enter your physics score: "))
History = int (input ("Enter your history score: "))
average = (Math + Physics + History) / 3
if average >= 10:
    print ("Educational Status: passed")
else:
    print ("Educational Status: failed")