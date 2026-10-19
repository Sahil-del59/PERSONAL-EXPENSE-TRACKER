import json
Filename="expenses.json"
def load_expenses():  # To know if file already existed or not
    try:
        with open ("expenses.json",'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def save_expenses(expenses): # To save current list of expenses in file
    with open ("expenses.json","w") as f:
        json.dump(expenses,f,indent=4)
def add_expenses(expenses): # To add new expenses to file
    amount=float(input("enter the amount"))
    category=input("enter the category")
    description=input("enter the description")
    d=dict(amount=amount,category=category,description=description)
    expenses.append(d)
    save_expenses(expenses)
    print("expenses saved succesfully")
def view_expenses(expenses): # To view expenses
    print(expenses)
def new(): # To ask the choice of user
    expenses=load_expenses()
    while True:
        print(".....expenses tracker.....")
        print("1,to add expenses")
        print("2 to view expenses")
        print("3 exit")
        choice=int(input("enter  your choice"))
        if choice==1:
            add_expenses(expenses)
        elif choice==2:
            view_expenses(expenses)
        elif choice==3:
            print("goodbye")
            break
        else:
            print("enter valid number")        
if __name__=="__main__":
    new()



