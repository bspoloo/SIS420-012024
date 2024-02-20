#Calculadora de matrices
import numpy as np;
def printMenu():
    print("======================================================================");
    print("Sum:                +");
    print("Rest:               -");
    print("Multiplication:     *");
    print("Show result:          R")
    print("======================================================================");


def isValid(n):
    if str(n).isdigit():
        return True;
    else:
        print("invalid number");
        return False;

def makeArray(rows, columns):
    array_rows = []
    for i in range(0,rows):
        array_columns = []
        for j in range(0,columns):
            data = int(input("Enter the data for position ({},{}) : ".format(i, j)))
            array_columns.append(data)
        array_rows.append(array_columns)
    return array_rows

def calculate(array, option):
    new_array =[];
    if option == "+":
        new_array = makeArray(rows, columns);
        create_array =np.array(new_array, int);
        
        print(create_array);
        array += create_array;
        print(array);
    elif option == "-":
        new_array = makeArray(rows, columns);
        create_array =np.array(new_array, int);
        array -= create_array;
    elif option == "*":
        new_array = makeArray(rows, columns);
        create_array =np.array(new_array, int);
        array.dot(create_array);
    return array;


printMenu();
acumulate = [];
rows = int(input("enter the number rows: "));
while not isValid(rows):
    rows = int(input("enter the correct number rows please: "));

columns = int(input("enter the number columns: "));
while not isValid(columns):
    columns = int(input("enter the correct number columns please: "));

init_array = makeArray(rows, columns);

userInput = "";

while not userInput == "R":
    printMenu()
    userInput = input("Select an operation: ")
    init_array = calculate(init_array, userInput)


print("Your array using this calculator is: ");
print(init_array);