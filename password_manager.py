from cryptography.fernet import Fernet

# generate key
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
'''

# load key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# master_pwd = input("What is the master password? ")

key = load_key() # + master_pwd.encode()
fer = Fernet(key)


# View password
def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

# Add password
def add():
    name = input("Account Name: ")
    passw = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(passw.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add password or view existing ones or quite (view/add/q): ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

