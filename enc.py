from cryptography.fernet import Fernet


print("Select your operation:\n")
pwd = input("1.add\n2.view\n3.quit\n")

def show_pas():
    with open('locked', 'r') as s:
        pass



def create_pwd():
    with open('locked', 'a') as s:
        s.writelines("this")

while True:
    if pwd == "add":
        create_pwd()
    elif pwd == "view":
        show_pass()
    elif quit = "quit":
        break
