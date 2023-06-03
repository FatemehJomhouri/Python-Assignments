
def read_from_database():
    file = open("Python/database.txt")
    for line in file:
        product = line.split(",")
        product = {"code":product[0],"name":product[1],"price":product[2],"count":product[3]}
        products.append(product)
        print("product:",product) 
def show_menu():
    print("1. add")
    print("2. edit")
    print("3. delete")
    print("4. buy")
    print("5. show products")
    print("6. search")
    print("7. exit")
def add():
    code=input("code: ")
    name=str(input("name: "))
    price=str(input("price: "))
    count=input("count: ")
    new_product={"code":code,"name":name,"price":price,"count":count}
    products.append(new_product)
def edit():
    user_input = input("Enter the keyword:")
    for product in products:
        if user_input==product["code"] or user_input==product["name"]:
            product_old=product
            print(product)
            user_input2=input("Please enter the variable that requires changing.('code','name','price','count'):")
            if user_input2 =="code":
                user_input3=(input("Enter the new code:"))
                for product in products:
                    if user_input3==product["code"]:
                        print("This code already exists")
                else :
                    product["code"]=user_input3
            elif user_input2 =="name":
                user_input3=(input("Enter the new name:"))
                for product in products:
                    if user_input3==product["name"]:
                        print("This name already exists")
                else:
                    product["name"]=user_input3
            elif user_input2=="price":
                user_input3=(input("Enter the new price:"))
                product["price"]=user_input3
            elif user_input2=="count":
                user_input3=(input("Enter the new count:"))
                product["count"]=user_input3
            else:
                print("this variable does not exist")
            break
    else:
        print("Not found")
    pass
def delete():
    user_input = input("Enter the keyword:")
    for product in products:
        if user_input==product["code"] or user_input==product["name"]:
            products.remove(product)
            print("It has been deleted")
            break
    else:
        print("Not found")
def buy():
    while True:
        user_input = input("Enter the keyword (or enter 'cancel' if you do not want to continue):")
        if user_input == "cancel":
            break
        for product in products:
            if user_input==product["code"] or user_input==product["name"]:
                user_count=int((input("how many of this item whould you like to buy:")))
                if int(product["count"]) >= user_count and user_count>0:
                    product["count"]=int(product["count"])-user_count
                    print("enjoy your shopping")
                else :
                    print("The count you requested is not available")
                break
            else:
                print("Not found")
                break

def show_products():
    print("code \t name \t price \t count")
    for i in range (len(products)):
        if products[i] is not "":
            print(products[i]["code"],"\t",products[i]["name"],products[i]["price"],products[i]["count"])
def search():
    user_input = input("Enter your keyword:")
    for product in products:
        if user_input==product["code"] or user_input==product["name"]:
            print(product)
            break
        else:
            print("Not found")
            break
def write():
    file=open("python/test30/database.txt","w")
    for i in range(len(products)):
        product=[products[i]["code"],products[i]["name"],products[i]["price"],products[i]["count"]]
        for j in range(len(product)):
            if j == 3 :
                list=product[j]
            else:
                list=product[j]+","
            file.write(list)
        file.write("")
products= []
read_from_database()
# print("products:",products)
while True:
    show_menu()
    user_choice=input("Select: ")
    if user_choice == "1":
        add()
    if user_choice == "2":
        edit()
    if user_choice == "3":
        delete()
    if user_choice == "4":
        buy()
    if user_choice == "5":
        show_products()
    if user_choice == "6":
        search()
    if user_choice == "7":
        write()
        exit()