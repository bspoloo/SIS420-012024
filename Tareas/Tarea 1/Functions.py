#Calculadora de matrices
#Sirve para calcular las matrices
import numpy as np;
def printMenu():
    print("======================================================================");
    print("Addition:                            A");
    print("Substraction:                        B");
    print("Multiplication:                      C");
    print("Scalar MUltiplication:               D")
    print("Array transposition:                 E")
    print("Determinant of a array:              F")
    print("Inverse of a array:                  G")
    print("Division:                            H")
    print("Scalar Product and vector product:   I")
    print("Show result:                         R")
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
            while not isValid(data):
                data = int(input("enter the correct number rows please: "));
            array_columns.append(data)
        array_rows.append(array_columns)
    return array_rows;

def multiScalar(array):
    scalar = int(input("enter scalar number: "));
    while not isValid(scalar):
        scalar = int(input("enter the correct scalar: "));
    
    return scalar*array;

def scalarVector():
    size = int(input("Enter size of array:"));
    while not isValid(size):
        size = int(input("Enter the correct size: "));

    print("Enter all data for vector 1");
    vector1 = makeArray(1,size);
    print("Enter all data for vector 1");
    vector2 = makeArray(1,size);
    scalar = np.dot(vector1, vector2);
    vectorial = np.cross(vector1, vector2);
    
    print("The scalar product is:");
    print(scalar);
    print("The vector product is:");
    print(vectorial);

def calculate(array, option):
    new_array =[];
    if option == "A":
        new_array = makeArray(rows, columns);
        create_array =np.array(new_array, int);
        array += create_array;
    elif option == "B":
        new_array = makeArray(rows, columns);
        create_array =np.array(new_array, int);
        array -= create_array;
    elif option == "C":
        new_array = makeArray(rows, columns);
        create_array =np.array(new_array, int);
        array = np.dot(array, create_array);
    elif option == "D":
        array = multiScalar(array);
    elif option == "E":
        array = [list(row) for row in zip(*array)];    
    elif option == "F":
        array =np.linalg.det(array);
    elif option == "G":
        array =np.linalg.inv(array);
    elif option == "H":
        inverse = np.linalg.inv(array);
        array =np.dot(array, inverse);
    elif option == "I":
        scalarVector();
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