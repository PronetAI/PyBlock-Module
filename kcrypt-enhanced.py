import random
import time
a = input("Enter your text here. ")
intrand1 = random.randint(1, 10000)
intrand2 = random.randint(1, 10000)


def Encrypt():
    global string
    string = ""
    for i in a:
        codeda = ord(i) * intrand1 + intrand2
        string = string + str(codeda)
    return string


def Decrypt(Input):
    global x
    for a in Input:
        a = ord(a) / intrand1 - intrand2
    askfortext = input("Enter your numbers here. ")
    time.sleep(1)
    if askfortext == string:
        return "Your text message is: " + Input
    elif askfortext == string:
        print()


print(Encrypt())
askencrypt = input("Do you want to decode your text? ")
time.sleep(1)
if askencrypt[0:1].upper() == "Y":
    try:
        print(Decrypt(a))
    except:
        print(Encrypt())
        print(Decrypt(a))
else:
    pass
