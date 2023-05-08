import random
numbers = []
n = int(input("Enter the list's lenghth: "))

while len(numbers) < n:
    num = random.randint(1, 1000)
    if numbers.count(num) == 0:
        numbers.append(num)


    
print(numbers)
