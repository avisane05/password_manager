master_pwd = input("What is the master password? ")

def view():
    pass

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd)

while True:
    mode = input("Would you like to add password or view existing ones or quite (view/add/q): ").lower()

    if mode == "q":
        break

    if mode == "view":
        pass
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

