# Enter the K-1 Encryption Code
def K_1():
    askforpassword = input("Enter your password here. ")
    for i in askforpassword:
        print(ord(i), end="")
