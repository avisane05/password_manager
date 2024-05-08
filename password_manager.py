pwd = input("What is the master password? ")

def view():
    pass

def add():
    pass

while True:
    mode = input("Would you like to add password or view existing ones or quite (view/add/q)").lower()

    if mode == "q":
        break

    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid mode.")
        continue

