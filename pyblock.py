# This is to install pip on OS
def OS_PIP_INSTALL():
    import os
    # Will reboot the window
    os.system('pip install --upgrade pip')
    os.system('pip install wheel')
    os.system('pip install twine')
    os.system('python example_project/setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')


# Standard Library for the RGB codes of the most basic colors and the Pip module
from Mod_Colors import *
from Get_Pip import *


# GENERAL FUNCTIONS
# This Shows anything on the Python Shell Interface
def Show(Text):
    # This Utilizes the Python print Command
    print(Text)


# Find out the type of the text
def Type(Text):
    print("Type:", type(Text))


# Take the User input
def Ask(Input):
    input(Input)


# LOGIC GATES
# This is the And Gate
def And_Gate(Input_1, Input_2):
    # Derived from the truth table
    if Input_1 == 0 and Input_2 == 0:
        return 0
    if Input_1 == 1 and Input_2 == 0:
        return 0
    if Input_1 == 0 and Input_2 == 1:
        return 0
    if Input_1 == 1 and Input_2 == 1:
        return 1


# This is the Or gate
def Or_Gate(Input_1, Input_2):
    # Derived from the truth table
    if Input_1 == 0 and Input_2 == 0:
        return 0
    if Input_1 == 1 and Input_2 == 0:
        return 1
    if Input_1 == 0 and Input_2 == 1:
        return 1
    if Input_1 == 1 and Input_2 == 1:
        return 1


# This is a not gate
def Not_Gate(Input_1):
    # Derived from the truth table
    if Input_1 == 0:
        return 1
    if Input_1 == 1:
        return 0


# This is a Nor Gate
def Nor_Gate(Input_1, Input_2):
    if Input_1 == 0 and Input_2 == 0:
        return 1
    if Input_1 == 1 and Input_2 == 0:
        return 0
    if Input_1 == 0 and Input_2 == 1:
        return 0
    if Input_1 == 1 and Input_2 == 1:
        return 0


# This is a Nand Gate
def Nand_Gate(Input_1, Input_2):
    if Input_1 == 1 and Input_2 == 1:
        return 0
    else:
        return 1


# This is an XNOR Gate
def XNOR_Gate(Input_1, Input_2):
    if Input_1 != Input_2:
        return 1
    else:
        return 0


# This is an XOR Gate
def XOR_Gate(Input_1, Input_2):
    if Input_1 == Input_2:
        return 1
    else:
        return 0


# STRING MATH
# Addition of Strings
def Str_Math(StrA, StrB):
    print(StrA + StrB)
