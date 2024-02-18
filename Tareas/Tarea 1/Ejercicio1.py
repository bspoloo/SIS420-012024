import numpy as np;

#creation of the array mxm 1
array_1 = np.array([
    [1,2,3,4],
    [5,5,7,8],
    [9,10,11,12],
    [13,14,15,16]
],int);

print(array_1);

#creation of the array MxM 2
array_2 = np.array([
    [2,5,64,5],
    [5,6,1,0],
    [9,120,23,34],
    [86,90,78,76]
],int);

print(array_2);
#Addition and Substraction of arrays MxM
#Addition of arrays MxM
Addition_1 = array_1 + array_2;
print("the Addition of the arrays MxM is:");
print(Addition_1);

#Substraction of arrays MxM
Substraction_1 = array_1 - array_2;
print("the Substraction of the arrays MxM is:");
print(Substraction_1);

#Substraction of arrays MxM
Substraction_1 = array_1 - array_2;
print("the Substraction of the arrays MxM is:");
print(Substraction_1);

#Multiplication of arrays MxM
Multiplication_1 = np.dot(array_1,array_2);
print("the Multiplication of the arrays MxM is:");
print(Multiplication_1);

#Division of arrays MxM
Division_1 = np.dot(array_1,array_2);
print("the Division of the arrays MxM is:");
print(Division_1);