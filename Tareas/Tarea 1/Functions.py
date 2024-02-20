#Calculadora de matrices
def printMenu():
    print("======================================================================");
    print("Sum:                +");
    print("Rest:               -");
    print("multiplication:     *");
    print("show resul:          R")
    print("======================================================================");


def isValid(n):
    if str(n).isdigit():
        return True;
    else:
        print("invalid number");
        return False;

def makeArray(rows, columns):
    array_rows = []
    for i in range(rows):
        array_columns = []
        for j in range(columns):
            data = int(input("Enter the data for position ({},{}) : ".format(i, j)))
            array_columns.append(data)
        array_rows.append(array_columns)
    return array_rows

def calculate(array, option):
    new_array =[];
    if option == "+":
        new_array = makeArray(rows, columns);
        array += new_array;
    elif option == "-":
        new_array = makeArray(rows, columns);
        array -= new_array;
    elif option == "*":
        new_array = makeArray(rows, columns);
        array.dot(new_array);
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

print(init_array);

while not userInput == "R":
    userInput =input("Select an operation: ");
    init_array = calculate(init_array, userInput);



print("Your array using this calculator is: ");
print(init_array);