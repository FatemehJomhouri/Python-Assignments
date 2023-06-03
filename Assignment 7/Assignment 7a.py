class Fraction:
    def init(self, soorat, makhraj):
        self.soorat = soorat
        self.makhraj = makhraj

    def show(self):
        print(self.soorat, "/", self.makhraj)

    def sum(self, second_fraction):
        result_fraction = Fraction((self.soorat * second_fraction.makhraj) + (second_fraction.soorat * self.makhraj), self.makhraj * second_fraction.makhraj)
        return result_fraction

    def subt(self, second_fraction):
        result_fraction = Fraction((self.soorat * second_fraction.makhraj) - (second_fraction.soorat * self.makhraj), self.makhraj * second_fraction.makhraj)
        return result_fraction

    def mult(self, second_fraction):
        result_fraction = Fraction(self.soorat * second_fraction.soorat, self.makhraj * second_fraction.makhraj)
        return result_fraction

    def division(self, second_fraction):
        if second_fraction.soorat == 0:
            print("Wrong values! the second fraction can not have 0.")
            return None

        result_fraction = Fraction(self.soorat * second_fraction.makhraj, self.makhraj * second_fraction.soorat)
        return result_fraction


while True:
    print("Enter calculation or not?")
    in_or_out = input("yes/no? ")
    if in_or_out == "no":
        break

    print("Welcome to the Fraction calculator. Enter the first fraction, then enter the second fraction, and finally choose your wished operation.")

    first_fraction = Fraction(None, None)
    first_fraction.soorat = float(input("Enter the numerator of the first fraction: "))
    first_fraction.makhraj = float(input("Enter the denominator of the first fraction: "))

    second_fraction = Fraction(None, None)
    second_fraction.soorat = float(input("Enter the numerator of the second fraction: "))
    second_fraction.makhraj = float(input("Enter the denominator of the second fraction: "))

    while first_fraction.makhraj == 0 or second_fraction.makhraj == 0:
        if first_fraction.makhraj == 0:
            print("Wrong values! The denominator of the first fraction can not be 0.")
            first_fraction.makhraj = float(input("Enter the denominator again: "))
        if second_fraction.makhraj == 0:
            print("Wrong values! The denominator of the second fraction can not be 0.")
            second_fraction.makhraj = float(input("Enter the denominator again: "))

    first_fraction.show()
    second_fraction.show()

    choice = input("Which operation do you want? (+), (-), (*), (/)? ")

    if choice == "+":
        result_fraction = first_fraction.sum(second_fraction)
    elif choice == "-":
        result_fraction = first_fraction.subt(second_fraction)
    elif choice == "*":
        result_fraction = first_fraction.mult(second_fraction)
    elif choice == "/":
        result_fraction = first_fraction.division(second_fraction)

    if result_fraction:
        result_fraction.show()